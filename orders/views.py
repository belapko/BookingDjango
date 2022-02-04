# from django.http import HttpResponseRedirect
# from django.shortcuts import render
#
#
# from basket.models import Basket
# from products.models import Product
# from orders.models import Order
# # Create your views here.
#
# def order_add(request, basket_id):
#     basket = Basket.objects.filter(id=basket_id)
#     product =
#     order = Order.objects.filter(user=request.user, product=product)
#
#
#     if not order.exists():
#         Order.objects.create(user=request.user, product=product, quantity=Order.order_quantity(basket))
#         return HttpResponseRedirect(request.META['HTTP_REFERER'])
from django.http import HttpResponseRedirect
from django.shortcuts import render

from basket.models import Basket
from orders.models import Order
from products.models import Product


def order_add(request, id):
    basket = Basket.objects.get(id=id)
    Order.objects.create(user=request.user, product=basket.product, quantity=basket.quantity)
    product = Product.objects.get(id=basket.product.id)
    product.quantity = 0
    product.save()
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def order_show(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders' : orders,
    }
    return render(request, 'orders/order.html', context)

def order_delete(request, id):
    order = Order.objects.get(id=id)
    product = Product.objects.get(id=order.product.id)
    product.quantity = product.standard_quantity
    product.save()
    order.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
