# Generated by Django 4.0.5 on 2022-08-06 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swoosh_app', '0059_rename_adresa_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='key',
        ),
    ]
