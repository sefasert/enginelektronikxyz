# Generated by Django 4.1.7 on 2023-03-12 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_related_product_benzerstok_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Osawa', 'osawa'), ('AXEN', 'axen'), ('INNOLUX', 'innolux'), ('SUNNY-AXEN', 'sunny-axen'), ('SANYO', 'sanyo'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Lifemaxx', 'lifemaxx'), ('ONVO', 'onvo'), ('AUO', 'auo'), ('BOE', 'boe'), ('YUMATU', 'yumatu'), ('MEGMEET', 'megmeet'), ('Premier', 'premier'), ('FSP', 'fsp'), ('PHILIPS', 'philips'), ('SHARP', 'sharp'), ('Vestel-Regal', 'vestel-regal'), ('SUNNY', 'sunny'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Homstar', 'homstar'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('SEG', 'seg'), ('REGAL', 'regal'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Dijitsu', 'dijitsu'), ('Vestel-SEG', 'vestel-seg'), ('Nordmende', 'nordmende'), ('LG', 'lg'), ('ROWELL', 'rowell'), ('Dreamstar', 'dreamstar'), ('Next', 'next'), ('Vestel', 'vestel'), ('Hisense', 'hisense'), ('AWOX', 'awox'), ('Vestel-Nexon', 'vestel-nexon'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Acer', 'acer'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Skytech', 'skytech'), ('NEXT', 'next'), ('SAMSUNG', 'samsung'), ('DARFON', 'darfon'), ('Profilo', 'profilo'), ('Vestel-ALBA', 'vestel-alba'), ('Panasonic', 'panasonic'), ('WOON', 'woon'), ('Hi-Level', 'hi-level'), ('-', ''), ('GEEPAS', 'geepas'), ('CHIMEI', 'chimei'), ('Navitech', 'navitech'), ('SONY', 'sony')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('2.EL', '2'), ('Sıfır', '0')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('Plazma', 'plazma'), ('LED', 'led'), ('LED-LCD', 'led-lcd'), ('LCD', 'lcd')], max_length=10),
        ),
    ]
