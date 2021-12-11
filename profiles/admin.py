from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'verified',
        'created_on',
    )


admin.site.register(UserProfile, UserProfileAdmin)
