# Generated by Django 2.2 on 2023-09-16 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230916_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='username',
            new_name='user_name',
        ),
    ]