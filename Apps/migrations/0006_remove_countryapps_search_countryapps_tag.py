# Generated by Django 4.0.4 on 2022-05-12 18:24

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('Apps', '0005_countryapps_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countryapps',
            name='search',
        ),
        migrations.AddField(
            model_name='countryapps',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]