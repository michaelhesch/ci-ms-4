# Generated by Django 3.2.9 on 2021-12-04 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'User Profiles'},
        ),
    ]