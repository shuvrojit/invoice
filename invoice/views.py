from django.views.generic import TemplateView, ListView
from .models import InvoiceModel

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
