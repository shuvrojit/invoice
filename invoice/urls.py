from django.urls import path

from . import views

urlpatterns = [
    path("add-new", views.AddNewPageView.as_view(), name="add-new"),
    path("history", views.HistoryPageView.as_view(), name="history"),
    path("", views.HomePageView.as_view(), name="invoice")
]
