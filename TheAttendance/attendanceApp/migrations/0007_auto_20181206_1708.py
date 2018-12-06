# Generated by Django 2.0.6 on 2018-12-06 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceApp', '0006_auto_20181206_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='username',
        ),
        migrations.AlterField(
            model_name='clockin',
            name='clockIn',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 17, 8, 59, 46625)),
        ),
        migrations.AlterField(
            model_name='clockout',
            name='clockOut',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 17, 8, 59, 47069)),
        ),
        migrations.DeleteModel(
            name='students',
        ),
    ]
