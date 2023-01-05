from django.contrib import admin
from .models import Size, Product, ProductItem, Category

admin.site.register(Category)
class SizeInline(admin.TabularInline):
    model = Size
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ("date","product","get_category" ,"code", "price", "available")
    list_filter = ("date", "price", "available")
    prepopulated_fields = {"slug": ("code",)}
    inlines = [SizeInline]

    def get_category(self, obj):
        return obj.product.category

    get_category.admin_order_field  = 'category'
    get_category.short_description = 'Category'

admin.site.register(ProductItem, ProductItemAdmin)



# @admin.register(InvoiceModel)
# class InvoiceAdmin(admin.ModelAdmin):
#     list_display = ("date", "status", "invoice_no", "parcel_id", "customer_name", "customer_address", "customer_mobile", "delivary_charge", "courier_charge", "invoice_amount", "receivable_amount", "courier_type", "order_by")
#     list_filter = ("date", "status", "invoice_amount", "courier_type", "order_by")
#     prepopulated_fields = {"slug": ("invoice_no",)}
