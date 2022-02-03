from django.shortcuts import render
from products.models import ProductCategory, Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    context = {
        'title': 'Чёрная икра',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'Выбор номера',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 4)  # Какой объект и сколько товаров на странице
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)  # Отображаем все элементы на странице
    context['products'] = products_paginator

    return render(request, 'products/products.html', context)
