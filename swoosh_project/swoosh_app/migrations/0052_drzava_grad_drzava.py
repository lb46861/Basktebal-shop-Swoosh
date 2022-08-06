# Generated by Django 4.0.5 on 2022-08-06 11:48

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('swoosh_app', '0051_grad_user_grad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drzava',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drzava', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='grad',
            name='drzava',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swoosh_app.drzava'),
        ),
    ]
