# Generated by Django 3.2.9 on 2021-12-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_billingaddress_order_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=4),
        ),
    ]