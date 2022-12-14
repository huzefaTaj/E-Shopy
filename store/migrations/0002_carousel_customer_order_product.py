# Generated by Django 3.2.9 on 2022-10-04 05:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5001)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default=None)),
                ('image', models.ImageField(blank=True, upload_to='uploads/products/')),
                ('image_url', models.CharField(blank=True, max_length=2083)),
                ('image_url2', models.CharField(blank=True, max_length=2083)),
                ('image_url3', models.CharField(blank=True, max_length=2083)),
                ('tag', models.CharField(blank=True, max_length=300)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=100)),
                ('postcode', models.IntegerField(default='0')),
                ('state', models.CharField(default='', max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('totalprice', models.IntegerField(default='0')),
                ('status', models.BooleanField(default=False)),
                ('orderid', models.CharField(blank=True, default='', max_length=500)),
                ('paymentid', models.CharField(blank=True, default='', max_length=500)),
                ('signatureid', models.CharField(blank=True, default='', max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('category', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
