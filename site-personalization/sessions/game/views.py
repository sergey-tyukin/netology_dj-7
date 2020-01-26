from django.shortcuts import render, redirect
from django.views import View
from django.db import transaction

from game.models import Game, Player, PlayerGameInfo
from game.forms import CreateForm, InputForm


template = 'home.html'


def _get_player(request):
    if not request.session.session_key:
        request.session.save()
    user_key = request.session.session_key

    current_player = Player.objects.filter(session_id=user_key).first()
    if not current_player:
        current_player = Player.objects.create(session_id=user_key)

    return current_player


def game(request, context={}, data={}):
    context['status'] = ''
    # Player gave an answer
    if data:
        if data['winner_other']:
            # Winner is other player
            context['status'] = 'end'
            context['answer'] = 'Победил другой игрок!'
            return render(request, template, context)

        context['tries'] = data['status'].tries_count
        if not data['current_game'].is_finished:
            # Wrong answer
            context['input_form'] = InputForm()
            context['tries'] = data['status'].tries_count
            return render(request, template, context)
        else:
            # Winner
            context['status'] = 'end'
            context['answer'] = 'Вы победили!'
            return render(request, template, context)

    current_player = _get_player(request)
    current_game = Game.objects.filter(creator=current_player, is_closed=False).last()

    # Game exist and Creator entered
    if current_game:
        if current_game.is_finished:
            # Game is finished
            context['status'] = 'creator_result'
            winner = PlayerGameInfo.objects.filter(game=current_game,
                                                   player=current_game.winner).last()
            context['tries'] = winner.tries_count
            current_game.is_closed = True
            current_game.save()
            return render(request, template, context)
        else:
            # Game must go on!
            context['status'] = 'creator_status'
            return render(request, template, context)

    current_game = Game.objects.filter(is_finished=False).last()
    status = PlayerGameInfo.objects.filter(game=current_game,
                                           player=current_player).last()

    # Game exist and player entered
    if current_game:
        # If new player
        if not status:
            status = PlayerGameInfo.objects.create(game=current_game,
                                                       player=current_player)
        context['tries'] = status.tries_count
        context['input_form'] = InputForm()
        context['key_min'] = current_game.key_min
        context['key_max'] = current_game.key_max
        return render(request, template, context)

    # Creating new game
    context['status'] = 'new'
    context['create_form'] = CreateForm()
    return render(request, template, context)


def create_game(request):
    context = {'status': 'error'}
    template = 'home.html'

    current_player = _get_player(request)

    game_form = CreateForm(request.POST)
    if not game_form.is_valid():
        context['errors'] = game_form.errors
        context['create_form'] = CreateForm()
        context['status'] = 'new'
        return render(request, template, context)

    key_min = game_form.cleaned_data['key_min']
    key_max = game_form.cleaned_data['key_max']
    key = game_form.cleaned_data['key']

    with transaction.atomic():
        current_game = Game.objects.create(key_min=key_min,
                                           key_max=key_max,
                                           key=key,
                                           creator=current_player)
        membership = PlayerGameInfo.objects.create(game=current_game,
                                                   player=current_player)

    # return render(request, template, context)
    return redirect('game')

def check_answer(request):
    context = {'status': 'error'}
    template = 'home.html'

    current_player = _get_player(request)
    current_game = Game.objects.filter(is_finished=False, players=current_player).last()
    status = PlayerGameInfo.objects.filter(game=current_game, player=current_player).last()

    input_form = InputForm(request.POST)
    if not input_form.is_valid():
        context['input_form'] = InputForm()
        context['key_min'] = current_game.key_min
        context['key_max'] = current_game.key_max
        context['errors'] = input_form.errors
        return render(request, template, context)

    key = input_form.cleaned_data['key']

    if not current_game:
        return game(request, context, {'winner_other': True})

    real_key = current_game.key

    status.tries_count += 1

    data = {
        'current_player': current_player,
        'current_game': current_game,
        'status': status,
        'is_winner': False,
        'winner_other': False
    }

    if key > real_key:
        context['answer'] = 'Загаданное число меньше'
    elif key < real_key:
        context['answer'] = 'Загаданное число больше'
    elif key == real_key:
        current_game.is_finished = True
        current_game.winner = current_player
        data['is_winner'] = True
        current_game.save()

    status.save()

    return game(request, context, data)