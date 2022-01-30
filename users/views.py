from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse

from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:  # if user - если есть в системе.
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Проверьте логин и пароль или создайте нового пользователя.')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Вход',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form' : form,
    }
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))