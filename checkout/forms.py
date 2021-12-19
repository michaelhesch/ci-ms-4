from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=250)
    phone = forms.CharField(max_length=20)
    address1 = forms.CharField(max_length=80,
                               label="Address", )
    address2 = forms.CharField(max_length=80,
                               label="Address 2 (optional)",
                               required=False)
    state = forms.CharField(max_length=50,
                            label="State", )
    city = forms.CharField(max_length=50,
                           label="City", )
    zipcode = forms.CharField(max_length=25,
                              label="Zipcode")
    country = CountryField(blank_label='Select Country').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))
    save_defaults = forms.BooleanField(
        widget=forms.CheckboxInput(),
        required=False)

    class Meta:
        fields = ('full_name', 'email', 'phone',
                  'address1', 'address2', 'state',
                  'city', 'zipcode', 'country',
                  'save_defaults')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address1': 'Address',
            'address2': 'Address Continued (Optional)',
            'state': 'State',
            'city': 'City',
            'zipcode': 'Zipcode',
            'country': 'Choose Country',
            'save_defaults': 'Save defaults to your profile?'
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            if self.fields['save_defaults']:
                self.fields['save_defaults'].label \
                    = "Save default shipping info?"
            else:
                pass
