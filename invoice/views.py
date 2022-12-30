from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import InvoiceModel, ProductModel
from .forms import ProductForm

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

def get_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm()

    return render(request, 'form.html', {'form': form})
