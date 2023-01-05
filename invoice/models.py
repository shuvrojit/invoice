from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    # slug = models.SlugField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    slug = models.SlugField()
    code = models.CharField(max_length=20)
    price = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date',)


class Size(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    size = models.CharField(max_length=6, null=True)
    quantity = models.IntegerField(null=True)


status_choices = [
    ("Pending", "Pending"),
    ("Delivered", "Delivered"),
    ("Courier", "Courier"),
    ("Exchange", "Exchange"),
    ("Cancel", "Cancel"),
    ("Return", "Return"),
]

courier_choices = [
    ("Pathao", "Pathao"),
    ("RedX", "RedX"),
]

# class InvoiceModel(models.Model):
#     date = models.DateField()
#     status = models.CharField(max_length=20, choices=status_choices, default="Delivered")
#     invoice_no = models.IntegerField()
#     slug = models.SlugField(unique=True)
#     parcel_id = models.CharField(max_length=250, blank=True, null=True)
#     customer_name = models.CharField(max_length=500)
#     customer_address = models.CharField(max_length=500)
#     customer_mobile = models.IntegerField()
#     products = models.ManyToManyField(ProductModel, related_name="products")
#     delivary_charge = models.IntegerField()
#     courier_charge = models.IntegerField()
#     invoice_amount = models.IntegerField()
#     receivable_amount = models.IntegerField(null=True)
#     courier_type = models.CharField(max_length=10, choices=courier_choices, default="Pathao")
#     order_by = models.CharField(max_length=250, blank=True)


#     def __str__(self):
#         return self.customer_name
