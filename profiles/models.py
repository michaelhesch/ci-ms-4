import random
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone = models.CharField(max_length=16, null=True, blank=True)
    default_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=50, null=True, blank=True)
    default_state = models.CharField(max_length=50, null=True, blank=True)
    default_zipcode = models.CharField(max_length=25, null=True, blank=True)
    default_country = CountryField(blank_label='Select Country', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username


class UserProfile(Profile):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username


class VendorProfile(UserProfile):
    store_name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    store_slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = 'Vendor Profiles'

    def __str__(self):
        return self.store_name

    def save(self, *args, **kwargs):
        if not self.store_name:
            random_value = random.randrange(10**1, 10**10)
            store_name = str(self.user.username) + str("'s Store") + str(random_value)
            self.store_name = store_name
        slug_name = str(self.store_name)
        self.store_slug = slugify(slug_name)
        super(VendorProfile, self).save(*args, **kwargs)

    def get_vendor_slug(self):
        return self.store_slug


@receiver(post_save, sender=User)
def create_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the user's profile
    """
    # If user profile is new, create new profile
    if created:
        VendorProfile.objects.create(user=instance)

    # If user profile exists already, save profile
    instance.userprofile.save()
