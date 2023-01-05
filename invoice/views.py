from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Product, ProductItem
from .forms import ProductForm, ProductItemForm

class HomePageView(TemplateView):
    """Home Page View"""
    template_name = "index.html"

def add_new_product_view(request):
    context = {}
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/add-product/')
    else:
        form = ProductForm()

    context['form'] = form
    return render(request, "add_product.html", context)


def add_new_product_item_view(request):
    context = {}
    form = ProductItemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products/')
    else:
        form = ProductItemForm()

    context['form'] = form
    return render(request, "add_product_item.html", context)

class ProductsPageView(ListView):
    model = ProductItem
    context_object_name = "productitems"
    template_name = "products.html"
