from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=20)
    price = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product} | {self.code}'

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

delivery_charge = [
    (70, "Inside Dhaka"),
    (130, "Outside Dhaka"),
]

class Customer(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    mobile = models.IntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=20, choices=status_choices, default="Delivered")
    invoice_no = models.IntegerField()
    parcel_id = models.CharField(max_length=250, blank=True, null=True)
    products = models.ManyToManyField(ProductItem, related_name="order", )
    delivery_charge = models.DecimalField(max_digits=7, decimal_places=2,choices=delivery_charge)
    courier_charge = models.DecimalField(max_digits=7, decimal_places=2)
    invoice_amount = models.DecimalField(max_digits=7, decimal_places=2)
    receivable_amount = models.DecimalField(max_digits=7, decimal_places=2)
    courier_type = models.CharField(max_length=10, choices=courier_choices, default="Pathao")
    order_by = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %Y %I:%M %p")}'



    class Meta:
        ordering = ("-created_on",)
