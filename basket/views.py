from django.shortcuts import render

from django.shortcuts import HttpResponseRedirect
from basket.models import Basket
from products.models import Product
# Create your views here.

# В КАЖДОЙ КОРЗИНЕ ОДИН ТОВАР

def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product) # Список корзин

    if not baskets.exists(): # Если список пустой - создаем
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER']) # Перенаправляем пользователя туда же где было выполнено действие
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
