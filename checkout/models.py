from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

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
    billing_address = models.ForeignKey('BillingAddress',
                                        on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True)

    def __str__(self):
        return self.user.username

    def get_grand_total(self):
        grand_total = 0
        for order_item in self.items.all():
            grand_total += order_item.get_item_total()
        return grand_total


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    address1 = models.CharField(max_length=80)
    address2 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=25)
    country = CountryField(multiple=False)
