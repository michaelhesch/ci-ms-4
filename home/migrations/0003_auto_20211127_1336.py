# Generated by Django 3.2.9 on 2021-11-27 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]