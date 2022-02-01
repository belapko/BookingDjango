from django.shortcuts import HttpResponseRedirect
from basket.models import Basket
from products.models import Product

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.

# В КАЖДОЙ КОРЗИНЕ ОДИН ТОВАР

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)  # Список корзин

    if not baskets.exists():  # Если список пустой - создаем
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(
            request.META['HTTP_REFERER'])  # Перенаправляем пользователя туда же где было выполнено действие
    else:
        basket = baskets.first()
        if basket.quantity < product.quantity:
            basket.quantity += 1
            basket.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, f'Номер рассчитан на {product.quantity} человек!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
