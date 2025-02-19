# Generated by Django 5.1.6 on 2025-02-19 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servReq', '0004_alter_request_datetimeadded_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='file',
        ),
        migrations.AlterField(
            model_name='request',
            name='dateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 19, 18, 42, 7, 641110)),
        ),
        migrations.AlterField(
            model_name='request',
            name='dateTimeResolved',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 19, 18, 42, 7, 641110)),
        ),
    ]
