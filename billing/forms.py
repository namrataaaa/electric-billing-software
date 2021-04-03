from django import forms
from .models import Customer

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'phone_number',
            'address',
        ]

class UserUpdateForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()