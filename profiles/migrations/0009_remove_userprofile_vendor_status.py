# Generated by Django 3.2.9 on 2021-12-14 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_rename_vendor_userprofile_vendor_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='vendor_status',
        ),
    ]