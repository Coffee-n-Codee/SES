# Generated by Django 3.1.7 on 2021-02-28 04:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210228_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 28, 4, 18, 8, 801003, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='last_day_register',
            field=models.DateField(default=datetime.datetime(2021, 2, 28, 4, 18, 8, 801003, tzinfo=utc)),
        ),
    ]