from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CheckoutForm(forms.Form):
    address1 = forms.CharField(max_length=80,
                               label="Address")
    address2 = forms.CharField(max_length=80,
                               label="Address 2 (optional)",
                               required=False)
    state = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=25)
    country = CountryField(blank_label='Select Country').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))
    billing_same = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    save_defaults = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
