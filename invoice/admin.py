from django.contrib import admin
from .models import ProductModel, InvoiceModel


admin.site.register(ProductModel)

@admin.register(InvoiceModel)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("date","invoice_no", "slug")
    prepopulated_fields = {"slug": ("invoice_no",)}
