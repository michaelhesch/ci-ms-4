from django.contrib import admin

from .models import UserProfile, VendorProfile


class VendorProfileAdmin(admin.ModelAdmin):
    model = VendorProfile
    """
    list_display = (
        'store_name',
    )
    """


class UserProfileAdmin(admin.ModelAdmin):


    list_display = (
        'user',
        'verified',
        'created_on',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(VendorProfile, VendorProfileAdmin)
