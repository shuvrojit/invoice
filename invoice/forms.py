from django.forms import ModelForm
# from django.conf import settings
# from django.template.loader import get_template
# from xhtml2pdf import pisa
from django import forms
from django.forms.models import inlineformset_factory

from .models import Product, ProductItem, Size, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["slug"]


class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        exclude = ["date", "slug"]

SizeFormSet = inlineformset_factory(
    ProductItem,
    Size,
    form=ProductItemForm,
    fields=("size", "quantity"),
    extra=6,
)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ["date", "slug"]
