from django.db import models

from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price*self.quantity

    @staticmethod
    def total_quantity(user):
        return sum(basket.quantity for basket in Basket.objects.filter(user=user))

    @staticmethod
    def total_sum(user):
        return sum(basket.sum() for basket in Basket.objects.filter(user=user))
