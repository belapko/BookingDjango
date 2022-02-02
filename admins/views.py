from django.shortcuts import render, HttpResponseRedirect

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from django.urls import reverse

from django.contrib.auth.decorators import user_passes_test
# Create your views here.

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'Админ-панель',
    }
    return render(request, 'admins/index.html', context)


# Create
@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'Создание пользователя',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


# Read
@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'title': 'Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


# Update
@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user =User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)  # instance для отображения полей объекта
    context = {
        'title': 'Обновление пользователя',
        'form' : form,
        'selected_user' : selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# Delete
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

# Activate user
@user_passes_test(lambda u: u.is_staff)
def admin_users_activate(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
