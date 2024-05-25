from django import forms
from .models import Customer

class CustomerSignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address','email','phonenumber','username']
