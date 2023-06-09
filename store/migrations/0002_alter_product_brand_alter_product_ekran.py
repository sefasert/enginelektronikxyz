# Generated by Django 4.1.7 on 2023-02-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('RONAX-TELENOVA', 'ronax-telenova'), ('GEEPAS', 'geepas'), ('Hisense', 'hisense'), ('Premier', 'premier'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('REGAL', 'regal'), ('Vestel-Regal', 'vestel-regal'), ('Skytech', 'skytech'), ('Dijitsu', 'dijitsu'), ('Navitech', 'navitech'), ('Homstar', 'homstar'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Profilo', 'profilo'), ('ROWELL', 'rowell'), ('SONY', 'sony'), ('SHARP', 'sharp'), ('Panasonic', 'panasonic'), ('BOE', 'boe'), ('SUNNY', 'sunny'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('ONVO', 'onvo'), ('Vestel-SEG', 'vestel-seg'), ('PHILIPS', 'philips'), ('Nordmende', 'nordmende'), ('SUNNY-AXEN', 'sunny-axen'), ('Vestel-ALBA', 'vestel-alba'), ('Hi-Level', 'hi-level'), ('Acer', 'acer'), ('INNOLUX', 'innolux'), ('Next', 'next'), ('AUO', 'auo'), ('SANYO', 'sanyo'), ('SEG', 'seg'), ('WOON', 'woon'), ('Dreamstar', 'dreamstar'), ('Vestel', 'vestel'), ('Lifemaxx', 'lifemaxx'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('-', ''), ('CHIMEI', 'chimei'), ('YUMATU', 'yumatu'), ('SAMSUNG', 'samsung'), ('NEXT', 'next'), ('Osawa', 'osawa'), ('DARFON', 'darfon'), ('LG', 'lg'), ('AWOX', 'awox'), ('AXEN', 'axen')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED-LCD', 'led-lcd'), ('LED', 'led'), ('LCD', 'lcd'), ('Plazma', 'plazma')], max_length=10),
        ),
    ]
