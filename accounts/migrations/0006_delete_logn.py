# Generated by Django 4.2.5 on 2023-10-04 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_username_logn_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='logn',
        ),
    ]
