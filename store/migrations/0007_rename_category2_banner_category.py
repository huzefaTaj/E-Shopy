# Generated by Django 3.2.9 on 2022-10-04 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_banner_category2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='category2',
            new_name='category',
        ),
    ]
