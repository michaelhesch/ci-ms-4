import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField


from product.models import Product
from profiles.models import UserProfile, VendorProfile


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
    create_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)
    shipping_details = models.ForeignKey('ShippingDetails',
                                        on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True)
    shipping = models.DecimalField(max_digits=4,
                                   decimal_places=2,
                                   null=False,
                                   default=10)
    grand_total = models.DecimalField(max_digits=12,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    
    class Meta:
        ordering = ['-order_date']

    # Generate random order number via private method for this class
    def _create_order_number(self):
        return uuid.uuid4().hex.upper()

    # Calculate grand total for all order items
    def update_grand_total(self):
        free_shipping = settings.FREE_DELIVERY_THRESHOLD
        self.grand_total = self.orderitems.aggregate(Sum('item_total'))['item_total__sum'] or 0
        if self.grand_total <= free_shipping:
            self.shipping = int(10)
        else:
            self.shipping = 0
        self.grand_total = self.grand_total + self.shipping
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
    vendor = models.ForeignKey(VendorProfile,
                               on_delete=models.CASCADE)
    item = models.ForeignKey(Product,
                             null=False,
                             blank=False,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    item_total = models.DecimalField(max_digits=12,
                                     decimal_places=2,
                                     null=False,
                                     blank=False,
                                     editable=False)
    ordered = models.BooleanField(default=False)
    vendor_amount = models.DecimalField(max_digits=12,
                                        decimal_places=2,
                                        editable=False)
    liffey_amount = models.DecimalField(max_digits=12,
                                        decimal_places=2,
                                        editable=False)
    vendor_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Order Items'
        ordering = ('-item_total',)

    def __str__(self):
        return f"{self.quantity} of {self.item.product_name} on {self.related_order}"

    # Calculate the total based on quantity of items in cart
    def get_item_total(self):
        return self.quantity * self.item.price

    # Returns the name of the seller's store
    def get_store_name(self):
        store = UserProfile.objects.get(user=self.item.seller)
        return store.store_name

    # Function to split vendor and store balances on order item
    def update_vendor_balance(self):
        self.liffey_amount= round(Decimal(self.item_total) * Decimal(0.05), 2)
        self.vendor_amount= round(Decimal(self.item_total) * Decimal(0.95), 2)

    # Function to update the line item total on save
    def save(self, *args, **kwargs):
        self.item_total = self.get_item_total()
        self.update_vendor_balance()
        super().save(*args, **kwargs)


class ShippingDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order_num = models.OneToOneField(Order, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=175)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=16)
    address1 = models.CharField(max_length=80)
    address2 = models.CharField(max_length=80,
                                blank=True,
                                null=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=25)
    country = CountryField(multiple=False)

    class Meta:
        verbose_name_plural = 'Shipping Details'

    def __str__(self):
        return f"{self.user.username}'s shipping details for {self.order_num}"
