# Generated by Django 3.2.9 on 2021-12-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(5, 'Five'), (4, 'Four'), (3, 'Three'), (2, 'Two'), (1, 'One')], default=5),
        ),
    ]
