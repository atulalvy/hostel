# Generated by Django 2.2.1 on 2020-03-12 11:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0018_auto_20200307_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='Date_of_birth',
            field=models.DateField(default=datetime.datetime(2020, 3, 12, 11, 1, 48, 772529, tzinfo=utc)),
        ),
    ]
