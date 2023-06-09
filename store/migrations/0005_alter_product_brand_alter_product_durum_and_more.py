# Generated by Django 4.1.7 on 2023-02-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('-', ''), ('Hisense', 'hisense'), ('AUO', 'auo'), ('Dreamstar', 'dreamstar'), ('Profilo', 'profilo'), ('Nordmende', 'nordmende'), ('Acer', 'acer'), ('Navitech', 'navitech'), ('REGAL', 'regal'), ('Osawa', 'osawa'), ('Vestel', 'vestel'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Vestel-ALBA', 'vestel-alba'), ('SONY', 'sony'), ('Vestel-Regal', 'vestel-regal'), ('SUNNY', 'sunny'), ('CHIMEI', 'chimei'), ('Next', 'next'), ('LG', 'lg'), ('SUNNY-AXEN', 'sunny-axen'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('SANYO', 'sanyo'), ('YUMATU', 'yumatu'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Hi-Level', 'hi-level'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Panasonic', 'panasonic'), ('AXEN', 'axen'), ('SEG', 'seg'), ('AWOX', 'awox'), ('Homstar', 'homstar'), ('Skytech', 'skytech'), ('PHILIPS', 'philips'), ('NEXT', 'next'), ('Vestel-SEG', 'vestel-seg'), ('Dijitsu', 'dijitsu'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('WOON', 'woon'), ('BOE', 'boe'), ('Lifemaxx', 'lifemaxx'), ('SAMSUNG', 'samsung'), ('INNOLUX', 'innolux'), ('GEEPAS', 'geepas'), ('ROWELL', 'rowell'), ('DARFON', 'darfon'), ('ONVO', 'onvo'), ('SHARP', 'sharp'), ('Premier', 'premier')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('Plazma', 'plazma'), ('LCD', 'lcd'), ('LED', 'led'), ('LED-LCD', 'led-lcd')], max_length=10),
        ),
    ]
