from django.contrib import admin
from .models import Size, Product, ProductItem, Category, Customer, Order
from django.utils.html import mark_safe

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)

class SizeInline(admin.TabularInline):
    model = Size
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ("date","product", "image", "description", "get_category" ,"code", "price", "available")
    list_filter = ("date", "price", "available")
    prepopulated_fields = {"slug": ("code",)}
    inlines = [SizeInline]

    def get_category(self, obj):
        return obj.product.category

    get_category.admin_order_field  = 'category'
    get_category.short_description = 'Category'

admin.site.register(ProductItem, ProductItemAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ("created_on", "status", "invoice_no", "parcel_id", "list_items", "delivery_charge", "courier_charge", "invoice_amount", "receivable_amount", "courier_type", "order_by")
    list_filter = ("created_on", "status", "courier_type", "order_by")
    prepopulated_fields = {"slug": ("invoice_no",)}


    # def list_items(self, obj):
        # return obj.products.all()

    def list_items(self, obj):
        # each obj will be an Order obj/instance/row
        to_return = '<ul>'
        # I'm assuming that there is a name field under the event.Product model. If not change accordingly.
        to_return += '\n'.join('<li>{}</li>'.format(item_name) for item_name in obj.products.values_list('product__name', flat=True))
        to_return += '</ul>'
        return mark_safe(to_return)

admin.site.register(Order, OrderAdmin)

class CustomerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Customer, CustomerAdmin)
