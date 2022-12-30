from django.urls import path

from . import views

urlpatterns = [
    # path("form", views.get_product, name="form"),
    path("products", views.ProductsPageView.as_view(), name="products"),
    path("invoicepdf", views.InvoicePdfView.as_view(), name="invoice"),
    # path("add-new", views.AddNewPageView.as_view(), name="add-new"),
    path("sales-report", views.HistoryPageView.as_view(), name="sales-report"),
    path("", views.HomePageView.as_view(), name="invoice")
]
