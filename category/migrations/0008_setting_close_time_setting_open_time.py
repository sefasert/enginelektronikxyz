# Generated by Django 4.1.3 on 2023-02-03 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_setting_copy_alter_setting_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='close_time',
            field=models.TimeField(default=datetime.time(21, 0)),
        ),
        migrations.AddField(
            model_name='setting',
            name='open_time',
            field=models.TimeField(default=datetime.time(10, 0)),
        ),
    ]
