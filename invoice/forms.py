from django.forms import ModelForm
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa

# from .models import InvoiceModel, ProductModel

# class InvoiceForm(ModelForm):

#     class Meta:
#         model = InvoiceModel
#         fields = ["invoice_no", "date", "customer_name","customer_address","customer_mobile", "delivary_charge"]


# class ProductForm(ModelForm):
#     class Meta:
#         model = InvoiceModel
#         fields = "__all__"

# class PdfForm(ModelForm):
