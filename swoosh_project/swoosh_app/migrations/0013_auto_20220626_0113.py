# Generated by Django 3.1.5 on 2022-06-25 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swoosh_app', '0012_auto_20220626_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='swoosh_app.role'),
        ),
    ]
