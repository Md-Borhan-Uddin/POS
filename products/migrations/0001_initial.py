# Generated by Django 4.2 on 2023-09-17 13:36

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
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Product Image')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Selling Price')),
                ('purches_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Purches Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='Product Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
