# Generated by Django 4.0 on 2021-12-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
