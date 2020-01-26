from django.shortcuts import render, redirect
from django.contrib import messages
from auth_reg.forms import CustomUserCreationForm


def home(request):
    context = {}
    return render(request, 'auth_reg/home.html', context)


def signup(request):
    context = {'form': CustomUserCreationForm()}
    template = 'auth_reg/signup.html'

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Аккаунт создан. Вы можете войти под учетной записью, '
                                      'либо создать нового пользователя')
            return redirect('home')
        else:
            context['errors'] = user_form.errors
            return render(request, template, context)

    return render(request, template, context)


# def login(request):
#     context = {}
#     return render(request, 'auth_reg/login.html', context)


def goodbye(request):
    context = {}
    return render(request, 'auth_reg/logout.html', context)
