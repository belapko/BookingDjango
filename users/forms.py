from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta: # Дополнительные поля с которыми работает основной класс UserLoginForm
        model = User
        fields = ('username', 'password')