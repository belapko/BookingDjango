from django.shortcuts import render

from products.models import ProductCategory, Product
# Create your views here.
def index(request):
    context = {
        'title' : 'Чёрная икра',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title' : 'Выбор номера',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)