from django.contrib import admin
from .models import UserProfile, VendorProfile


class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'verified',
        'created_on',
    )


class VendorProfileAdmin(admin.TabularInline):
    model = VendorProfile
    
    list_display = (
        'store_owner',
        'store_name',
        'vendor_balance',
    )


admin.site.register(UserProfile, UserProfileAdmin)
