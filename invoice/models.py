from django.db import models


class ProductModel(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=250, null=True)
    code = models.CharField(max_length=20)
    price = models.IntegerField()
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class SizeModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    size = models.CharField(max_length=6, null=True)
    quantity = models.IntegerField(null=True)


status_choices = [
    (0, "Pending"),
    (1, "Delivered"),
    (2, "Courier"),
    (3, "Exchange"),
    (4, "Cancel"),
    (5, "Return"),
]

courier_choices = [
    (0, "Pathao"),
    (1, "RedX"),
]

class InvoiceModel(models.Model):

    date = models.DateField()
    status = models.CharField(max_length=20, choices=status_choices, default="Delivered")
    invoice_no = models.IntegerField()
    slug = models.SlugField(unique=True)
    parcel_id = models.CharField(max_length=250, blank=True, null=True)
    customer_name = models.CharField(max_length=500)
    customer_address = models.CharField(max_length=500)
    customer_mobile = models.IntegerField()

    delivary_charge = models.IntegerField()
    courier_charge = models.IntegerField()
    invoice_amount = models.IntegerField()
    recievable_amount = models.IntegerField(null=True)
    courier_type = models.CharField(max_length=10, choices=courier_choices, default="Pathao")
    order_by = models.CharField(max_length=250, blank=True)


    def __str__(self):
        return self.customer_name
