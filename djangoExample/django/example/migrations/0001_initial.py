# Generated by Django 3.0.6 on 2020-05-18 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=7)),
                ('vin_number', models.CharField(max_length=17)),
                ('purchase_date', models.DateField(default=datetime.date(2020, 5, 18))),
                ('miles', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
