from django import forms
from .models import Customers

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = ('first_name', 'last_name', 'date_of_birth', 'phone_number')
