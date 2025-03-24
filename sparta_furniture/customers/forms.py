from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Mata:
        model = Customer
        fields = [
            "customer_id",
            "customer_name",
            "customer_tell",
        ]
        exclude = [
            "customer_create_at",
        ]


class Customer_UpdateForm(forms.ModelForm):
    class Mata:
        model = Customer
        fields = [
            "customer_name",
            "customer_tell",
        ]
        exclude = [
            "customer_create_at",
            "customer_id",
            
        ]