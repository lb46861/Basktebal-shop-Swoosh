# Generated by Django 3.1.5 on 2022-06-25 14:28

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('swoosh_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Uloge',
            new_name='Role',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]