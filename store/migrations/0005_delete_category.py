# Generated by Django 4.0 on 2021-12-15 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
