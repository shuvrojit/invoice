from django.urls import path

from . import views

urlpatterns = [
    # path("form", views.get_product, name="form"),
    path("products/", views.ProductsPageView.as_view(), name="products"),
    # path("invoicepdf", views.InvoicePdfView.as_view(), name="invoice"),
    path("add-product-item/", views.add_new_product_item_view, name="add-item"),
    path("add-product/", views.add_new_product_view, name="add-product"),
    path("sales-report", views.OrderView.as_view(), name="sales-report"),
    path("", views.HomePageView.as_view(), name="invoice")
]
