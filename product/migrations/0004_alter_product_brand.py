# Generated by Django 3.2.9 on 2021-12-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20211213_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('AMD', 'AMD'), ('ASUS', 'ASUS'), ('EVGA', 'EVGA'), ('GIGABYTE', 'GIGABYTE'), ('MSI', 'MSI'), ('Nvidia', 'Nvidia'), ('SAPPHIRE', 'SAPPHIRE'), ('XFX', 'XFX')], max_length=120),
        ),
    ]
