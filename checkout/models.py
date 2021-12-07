import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from liffey.settings import FREE_DELIVERY_THRESHOLD
from django_countries.fields import CountryField


from product.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_num = models.CharField(max_length=32,
                                 null=False,
                                 editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             related_name='orders')
    items = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress',
                                        on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True)
    shipping = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=10)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    
    # Generate random order number via private method for this class
    def _create_order_number(self):
        return uuid.uuid4().hex.upper()

    # Calculate grand total for all order items
    def update_grand_total(self):
        grand_total = 0
        self.grand_total = self.lineitems.aggregate(Sum('item_total'))['item_total__sunm']
        if self.grand_total < FREE_DELIVERY_THRESHOLD:
            self.shipping = int(10)
        else:
            self.shipping = 0
        grand_total = self.grand_total + self.shipping
        self.grand_total = grand_total
        self.save()

    # Calculate total number of all order items in order
    def get_total_item_count(self):
        item_count = 0
        for order_item in self.items.all():
            item_count += order_item.quantity
        return item_count

    # Override standard save method to set order number
    def save(self, *args, **kwargs):
        if not self.order_num:
            self.order_num = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Order Number: %s" % self.order_num


class OrderItem(models.Model):
    related_order = models.ForeignKey(Order,
                                      null=False,
                                      blank=False,
                                      on_delete=models.CASCADE,
                                      related_name='orderitems')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    item_total = models.DecimalField(max_digits=6,
                                     decimal_places=2,
                                     null=False,
                                     blank=False,
                                     editable=False)

    class Meta:
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.quantity} of {self.item.product_name} on order {self.related_order}"

    # Calculate the total based on quantity of items in cart
    def get_item_total(self):
        return self.quantity * self.item.price

    # Returns the name of the seller's store
    def get_store_name(self):
        store = UserProfile.objects.get(user=self.item.seller)
        return store.store_name

    def save(self, *args, **kwargs):
        self.item_total = self.get_item_total()
        super().save(*args, **kwargs)


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order_num = models.OneToOneField(Order, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=80)
    address2 = models.CharField(max_length=80,
                                blank=True,
                                null=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=25)
    country = CountryField(multiple=False)

    class Meta:
        verbose_name_plural = 'Billing Addresses'

    def __str__(self):
        return "%s's billing address" % self.user.username
