# Generated by Django 4.0.4 on 2022-05-11 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cities', '0003_alter_cities_citi_main_slug_alter_cities_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=60, unique=True)),
            ],
            options={
                'ordering': ['-tag'],
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url_on_map', models.URLField()),
                ('entry_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True)),
                ('best_time_togo', models.TextField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit', to='Cities.listofcities')),
                ('tags', models.ManyToManyField(to='Visit.filterby')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]