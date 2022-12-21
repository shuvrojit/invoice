from django.db import models


class ProductModel(models.Model):
    product_code = models.CharField(max_length=20)
    product_size = models.CharField(max_length=5)
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_code

class InvoiceModel(models.Model):

    invoice_no = models.IntegerField()
    slug = models.SlugField(unique=True, null=True)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_mobile = models.IntegerField()

    products = models.ForeignKey(ProductModel, related_name="products", on_delete=models.CASCADE)

    delivary_charge = models.IntegerField()
    tax = models.IntegerField()


    def __str__(self):
        return self.customer_name


