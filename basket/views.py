from django.shortcuts import HttpResponseRedirect
from basket.models import Basket
from products.models import Product

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.http import JsonResponse

from orders.models import Order

# Create your views here.

# В КАЖДОЙ КОРЗИНЕ ОДИН ТОВАР

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)  # Список корзин

    if not baskets.exists():  # Если список пустой - создаем
        if product.quantity == 0:
            messages.error(request, 'Номер забронирован!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Перенаправляем пользователя туда же где было выполнено действие
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


#####
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


#####

def basket_edit(request, id, quantity):  # basket_id, basket_quantity
    if is_ajax(request=request):
        basket = Basket.objects.get(id=id)
        if quantity > 0 and quantity <= basket.product.quantity:
            basket.quantity = quantity
            basket.save()
        elif quantity == 0:
            basket.delete()
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'baskets': baskets
    }
    result = render_to_string('basket/basket.html', context)  # Рендер страницы с обновлённым контекстом
    return JsonResponse({'result': result})






