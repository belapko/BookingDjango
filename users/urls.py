from django.urls import path

from users.views import login, registration, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('regitration/', registration, name='registration'),
        path('logout/', logout, name='logout')
]