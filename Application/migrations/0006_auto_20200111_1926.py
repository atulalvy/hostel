# Generated by Django 2.2.1 on 2020-01-11 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0005_applications_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='Date_of_birth',
            field=models.DateField(default=datetime.datetime(2020, 1, 11, 13, 56, 22, 504862, tzinfo=utc)),
        ),
    ]
