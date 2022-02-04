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


