# Generated by Django 4.1.3 on 2022-12-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_setting_adres_setting_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='saat',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
