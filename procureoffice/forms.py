from dataclasses import fields
from django.forms import ModelForm
from .models import *
from django import forms

from .models import(Product, Supplier)


# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'product_name', 'product_price', 'department' ]
        widgets = {
            'product_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'product_price': forms.TextInput(attrs={ 'class': 'form-control' }),
            'department': forms.TextInput(attrs={ 'class': 'form-control' }),
        }

#Purchase Request form 
class PurchaseRequestForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequest
        fields = ['pr_no', 'pr_status', ]


class PurchaseRequestForm(ModelForm):
    class Meta:
        model = PurchaseRequest
        fields = '__all__'


#Purchase Order form
class PurchaseOrderForm(forms.ModelForm):
    class Meta: 
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderItem(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = "__all__"

#Supplier form
class SupplierForm(forms.ModelForm):
    class Meta: 
        model = Supplier
        fields = ['company_name', 'contact_name', 'contact_email', 'phone', 'alternative_phone', 'website', 'address', ]
        widgets = {
            'company_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contact_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contact_email': forms.TextInput(attrs={ 'class': 'form-control' }),
            'phone': forms.TextInput(attrs={ 'class': 'form-control' }),
            'alternative_phone': forms.TextInput(attrs={ 'class': 'form-control' }),
            'website': forms.TextInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
        }

