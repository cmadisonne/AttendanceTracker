# Generated by Django 2.0.6 on 2018-12-05 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceApp', '0002_auto_20181205_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemodel',
            name='clockIn',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='attendancemodel',
            name='clockOut',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
