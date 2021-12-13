# Generated by Django 3.2.9 on 2021-12-13 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20211213_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='vendor_profile',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='store_owner',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='vendor_balance',
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='userprofile_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='vendor_balance_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='vendor_balance_unpaid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]