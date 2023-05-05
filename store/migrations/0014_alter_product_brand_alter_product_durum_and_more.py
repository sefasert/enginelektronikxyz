# Generated by Django 4.1.7 on 2023-03-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_product_brand_alter_product_ekran_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('PHILIPS', 'philips'), ('AXEN', 'axen'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Premier', 'premier'), ('RONAX-TELENOVA', 'ronax-telenova'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Osawa', 'osawa'), ('YUMATU', 'yumatu'), ('Hi-Level', 'hi-level'), ('BOE', 'boe'), ('Navitech', 'navitech'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('LG', 'LG'), ('INNOLUX', 'innolux'), ('Vestel-Regal', 'vestel-regal'), ('Skytech', 'skytech'), ('Dreamstar', 'dreamstar'), ('Homstar', 'homstar'), ('-', ''), ('GEEPAS', 'geepas'), ('SEG', 'seg'), ('Panasonic', 'panasonic'), ('MEGMEET', 'megmeet'), ('SUNNY', 'Sunny'), ('WOON', 'woon'), ('CHIMEI', 'chimei'), ('SANYO', 'sanyo'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Hisense', 'hisense'), ('DARFON', 'darfon'), ('REGAL', 'regal'), ('Vestel-SEG', 'vestel-seg'), ('SAMSUNG', 'Samsung'), ('Dijitsu', 'dijitsu'), ('Vestel-ALBA', 'vestel-alba'), ('Profilo', 'profilo'), ('ROWELL', 'rowell'), ('SUNNY-AXEN', 'sunny-axen'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Next', 'next'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('AUO', 'auo'), ('SHARP', 'sharp'), ('Acer', 'acer'), ('Vestel-Nexon', 'vestel-nexon'), ('Nordmende', 'nordmende'), ('NEXT', 'next'), ('SONY', 'sony'), ('VESTEL', 'Vestel'), ('Lifemaxx', 'lifemaxx'), ('ONVO', 'onvo'), ('FSP', 'fsp'), ('AWOX', 'awox')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('2.EL', '2'), ('Sıfır', '0')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('Plazma', 'plazma'), ('LCD', 'lcd'), ('LED', 'led'), ('LED-LCD', 'led-lcd')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
