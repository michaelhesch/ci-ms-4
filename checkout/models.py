from django.db import models
from django.conf import settings

from product.models import Product


class OrderItem(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.product_name}"

    # Calculate the total based on quantity of items in cart
    def get_item_total(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    create_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_grand_total(self):
        grand_total = 0
        for order_item in self.items.all():
            grand_total += order_item.get_item_total()
        return grand_total
