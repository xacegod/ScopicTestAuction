# Generated by Django 3.2.7 on 2021-09-03 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0003_auto_20210903_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bidder_id',
            new_name='bidder',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='bidder_id',
            new_name='bidder',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='seller_id',
            new_name='seller',
        ),
        migrations.AlterField(
            model_name='item',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 4, 6, 6, 6, 576658, tzinfo=utc)),
        ),
    ]
