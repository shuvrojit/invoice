from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import InvoiceModel, ProductModel
from django.views.generic.detail import DetailView
from django_xhtml2pdf.views import PdfMixin

class HomePageView(TemplateView):
    """Home Page View"""
    template_name = "index.html"

class AddNewPageView(TemplateView):
    """Add New Page View"""
    template_name = "add_new.html"

class HistoryPageView(ListView):
    """History Page View"""
    model = InvoiceModel
    context_object_name = "invoices"
    template_name = "history.html"

class ProductsPageView(ListView):
    model = ProductModel
    context_object_name = "products"
    template_name = "products.html"

class InvoicePdfView(PdfMixin, DetailView):
    model = InvoiceModel
    context_object_name = "invoices"
    template_name = "invoice_pdf.html"
