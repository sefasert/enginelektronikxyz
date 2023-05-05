# Generated by Django 4.1.7 on 2023-02-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_brand_alter_product_ekran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Vestel-ALBA', 'vestel-alba'), ('SONY', 'sony'), ('GEEPAS', 'geepas'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Vestel-Regal', 'vestel-regal'), ('Lifemaxx', 'lifemaxx'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('AWOX', 'awox'), ('Dreamstar', 'dreamstar'), ('ROWELL', 'rowell'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Next', 'next'), ('YUMATU', 'yumatu'), ('SAMSUNG', 'samsung'), ('Vestel-SEG', 'vestel-seg'), ('Nordmende', 'nordmende'), ('Vestel', 'vestel'), ('BOE', 'boe'), ('-', ''), ('LG', 'lg'), ('DARFON', 'darfon'), ('WOON', 'woon'), ('REGAL', 'regal'), ('Navitech', 'navitech'), ('ONVO', 'onvo'), ('Acer', 'acer'), ('CHIMEI', 'chimei'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Homstar', 'homstar'), ('AXEN', 'axen'), ('Dijitsu', 'dijitsu'), ('INNOLUX', 'innolux'), ('Osawa', 'osawa'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SANYO', 'sanyo'), ('PHILIPS', 'philips'), ('SUNNY-AXEN', 'sunny-axen'), ('Hisense', 'hisense'), ('SEG', 'seg'), ('SHARP', 'sharp'), ('AUO', 'auo'), ('Panasonic', 'panasonic'), ('Profilo', 'profilo'), ('RONAX-TELENOVA', 'ronax-telenova'), ('SUNNY', 'sunny'), ('NEXT', 'next'), ('Premier', 'premier'), ('Hi-Level', 'hi-level'), ('Skytech', 'skytech')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('2.EL', '2'), ('Sıfır', '0')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('Plazma', 'plazma'), ('LED', 'led'), ('LCD', 'lcd'), ('LED-LCD', 'led-lcd')], max_length=10),
        ),
    ]
