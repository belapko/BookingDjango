from django.contrib import admin

from basket.models import Basket
# Register your models here.

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0