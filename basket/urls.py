from django.urls import path
from basket.views import basket_add

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'), # Передаем product id
]