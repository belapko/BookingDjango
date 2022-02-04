from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect

import users.views
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfileFormAdd
from django.contrib import auth
from django.urls import reverse

from django.contrib import messages
from basket.models import Basket

from django.contrib.auth.decorators import login_required
from djangoProject import settings

# Create your views here.
from users.models import User


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
            messages.error(request, 'Неверный логин и/или пароль!')
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
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, f'На вашу почту отправлено письмо для подтверждения!')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


@transaction.atomic  # Если одна из форм не сработает - откат всех изменений
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, files=request.FILES, data=request.POST)
        profile_form = UserProfileFormAdd(request.POST, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)  # instance для отображения полей объекта
        profile_form = UserProfileFormAdd(instance=request.user.userprofile)
    context = {
        'title': 'Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
        'profile_form' : profile_form,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=(user.email, user.activation_key))

    title = f'Подтвреждение учетной записи {user.username}'
    message = f'Для подтвреждения учетной записи {user.username} гостиницы "Чёрная Икра" перейдите по ссылке: {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            return HttpResponseRedirect(reverse('users:login'))
    except Exception as e:
        return HttpResponseRedirect(reverse('users:login'))
