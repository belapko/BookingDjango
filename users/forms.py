from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:  # Дополнительные поля с которыми работает основной класс UserLoginForm
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите email адрес'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Имя пользователя', 'readonly' : True }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Адрес электронной почты', 'readonly' : True }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Фамилия'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'custom-file-input', 'placeholder' : 'Выберите изображение' }), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')