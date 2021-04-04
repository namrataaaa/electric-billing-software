# Generated by Django 3.1.7 on 2021-04-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billinformation',
            name='energy_units_consumed',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
