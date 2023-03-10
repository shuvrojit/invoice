# Generated by Django 4.1.4 on 2023-01-06 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('mobile', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('code', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.product')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=6, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.productitem')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Courier', 'Courier'), ('Exchange', 'Exchange'), ('Cancel', 'Cancel'), ('Return', 'Return')], default='Delivered', max_length=20)),
                ('invoice_no', models.IntegerField()),
                ('parcel_id', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_charge', models.DecimalField(choices=[(70, 'Inside Dhaka'), (130, 'Outside Dhaka')], decimal_places=2, max_digits=7)),
                ('courier_charge', models.DecimalField(decimal_places=2, max_digits=7)),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('receivable_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('courier_type', models.CharField(choices=[('Pathao', 'Pathao'), ('RedX', 'RedX')], default='Pathao', max_length=10)),
                ('order_by', models.CharField(blank=True, max_length=250)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.customer')),
                ('products', models.ManyToManyField(related_name='order', to='invoice.productitem')),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]
