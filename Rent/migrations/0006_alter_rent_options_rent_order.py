# Generated by Django 4.0.4 on 2022-06-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0005_alter_rent_apartment_alter_rent_guest_house_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rent',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='rent',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
