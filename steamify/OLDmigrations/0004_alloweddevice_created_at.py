# Generated by Django 2.2.4 on 2019-10-26 03:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('steamify', '0003_auto_20191025_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='alloweddevice',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 3, 47, 17, 59263, tzinfo=utc)),
            preserve_default=False,
        ),
    ]