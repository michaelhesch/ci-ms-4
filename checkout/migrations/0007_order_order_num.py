# Generated by Django 3.2.9 on 2021-12-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_billingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_num',
            field=models.CharField(default=12345778, editable=False, max_length=32),
            preserve_default=False,
        ),
    ]
