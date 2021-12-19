from django import forms

from .models import VendorProfile


class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = [
            'store_name',
        ]
