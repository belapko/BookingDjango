from django.db import models

# Create your models here.
# Таблицы в БД

class ProductCategory(models.Model):  # Поле id по умолчанию создается внутри класса Model
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True) # Не обязательно заполнять. Пустое поле по умолчанию

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    quantity = models.PositiveIntegerField(default=0)
    standard_quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} | {self.category.name}'