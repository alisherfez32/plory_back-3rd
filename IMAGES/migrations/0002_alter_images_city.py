# Generated by Django 4.0.4 on 2022-05-11 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0004_cities_search_countries_search'),
        ('IMAGES', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_images', to='Cities.listofcities'),
        ),
    ]
