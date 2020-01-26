from django.db import models


class Game(models.Model):
    key_min = models.IntegerField()
    key_max = models.IntegerField()
    key = models.IntegerField()
    players = models.ManyToManyField('Player', through='PlayerGameInfo', related_name='game')
    is_finished = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    creator = models.ForeignKey('Player', on_delete=models.DO_NOTHING,
                               related_name='create_game')
    winner = models.ForeignKey('Player', on_delete=models.DO_NOTHING,
                               related_name='win_game', null=True)


class Player(models.Model):
    session_id = models.CharField(max_length=32, editable=False)


class PlayerGameInfo(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='status')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='status')
    # is_player_creator = models.BooleanField(default=False)
    # get_result = models.BooleanField(default=False)
    tries_count = models.IntegerField(default=0)
