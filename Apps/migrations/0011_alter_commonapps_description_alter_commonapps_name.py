# Generated by Django 4.0.4 on 2022-06-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0010_alter_commonapps_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonapps',
            name='description',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commonapps',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]