# Generated by Django 3.2.9 on 2021-12-05 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
    ]
