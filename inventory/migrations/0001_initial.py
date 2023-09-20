# Generated by Django 4.2 on 2023-09-20 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Quantity')),
                ('offer', models.PositiveIntegerField(blank=True, null=True, verbose_name='Offer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='products.product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('purches_quentity', models.PositiveIntegerField(verbose_name='Purches')),
                ('sales_quentity', models.PositiveIntegerField(verbose_name='Sales')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='store', to='products.product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('invoice_no', models.CharField(default='0000', max_length=255, unique=True, verbose_name='invoice No')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('offer', models.PositiveIntegerField(blank=True, null=True, verbose_name='Offer')),
                ('is_pay', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('sale_product', models.ManyToManyField(related_name='sale_product', to='inventory.saleproduct', verbose_name='Product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_invoice', to=settings.AUTH_USER_MODEL, verbose_name='Seller')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Quantity')),
                ('offer', models.PositiveIntegerField(blank=True, null=True, verbose_name='Offer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purches', to='products.product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
