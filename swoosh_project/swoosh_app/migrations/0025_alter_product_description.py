# Generated by Django 4.0.5 on 2022-06-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swoosh_app', '0024_product_material_alter_product_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]