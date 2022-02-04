from django.contrib import admin

# Register your models here.
from products.models import Product, ProductCategory

admin.site.register(ProductCategory)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity', 'category', 'standard_quantity'), 'image')
    search_fields = ('name',)
    ordering = ('category',)