# Generated by Django 4.0.4 on 2022-05-08 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0003_alter_cities_citi_main_slug_alter_cities_country_and_more'),
        ('Transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transport', to='Cities.countries'),
        ),
    ]
