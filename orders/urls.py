# from django.urls import path
# from orders.views import order_add
#
# app_name = 'orders'
#
# urlpatterns = [
#     path('add/<int:basket_id>/', order_add, name='order_add'),
# ]
from django.urls import path

from orders.views import order_add, order_delete

app_name = 'orders'

urlpatterns = [
    path('order/<int:id>/', order_add, name='order_add'),
    path('delete/<int:id>/', order_delete, name='order_delete')
]
