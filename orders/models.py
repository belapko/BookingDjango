from django.db import models

from users.models import User
from products.models import Product
from basket.models import Basket
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def order_quantity(self):
        basket = Basket.objects.get(user=self.user)
        quantity = basket.quantity
        return quantity