from django.urls import path

from . import views

urlpatterns = [
    path("form", views.get_product, name="form"),
    path("products", views.ProductsPageView.as_view(), name="products"),
    path("add-new", views.AddNewPageView.as_view(), name="add-new"),
    path("history", views.HistoryPageView.as_view(), name="history"),
    path("", views.HomePageView.as_view(), name="invoice")
]
