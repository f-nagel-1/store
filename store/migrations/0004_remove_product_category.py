# Generated by Django 4.0 on 2021-12-15 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
