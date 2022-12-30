from django.contrib import admin
from .models import SizeModel, ProductModel, InvoiceModel

class SizeAdminInline(admin.TabularInline):
    model = SizeModel
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "code", "price", "available")
    list_filter = ("date", "name", "price", "available")
    inlines = [SizeAdminInline,]

admin.site.register(ProductModel, ProductAdmin)


@admin.register(InvoiceModel)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("date","invoice_no", "slug")
    prepopulated_fields = {"slug": ("invoice_no",)}
