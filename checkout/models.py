from django.db import models
from django.conf import settings

from product.models import Product


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    create_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
