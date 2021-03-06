# Generated by Django 4.0 on 2021-12-21 11:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_orderitem_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 21, 11, 40, 53, 318062, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 21, 11, 41, 7, 876780, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
