# Generated by Django 4.0.4 on 2022-05-08 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0002_alter_commonapps_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryapps',
            name='slug',
            field=models.SlugField(default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Cities.countries')),
        ),
    ]
