from django.contrib import admin
from .models import SizeModel, ProductModel, InvoiceModel

class SizeAdminInline(admin.TabularInline):
    model = SizeModel
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "code", "price", "available")
    list_filter = ("date", "name", "price", "available")
    prepopulated_fields = {"slug": ("code",)}
    inlines = [SizeAdminInline,]

admin.site.register(ProductModel, ProductAdmin)


@admin.register(InvoiceModel)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("date", "status", "invoice_no", "parcel_id", "customer_name", "customer_address", "customer_mobile", "delivary_charge", "courier_charge", "invoice_amount", "receivable_amount", "courier_type", "order_by")
    list_filter = ("date", "status", "invoice_amount", "courier_type", "order_by")
    prepopulated_fields = {"slug": ("invoice_no",)}
