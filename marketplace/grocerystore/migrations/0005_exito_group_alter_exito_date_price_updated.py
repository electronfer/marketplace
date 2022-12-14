# Generated by Django 4.1 on 2022-10-31 01:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0004_alter_exito_date_price_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='exito',
            name='group',
            field=models.CharField(choices=[('FOOD', 'Food'), ('CLEANING', 'Cleaning'), ('VEGETABLES', 'Vegetables')], default='Food', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='exito',
            name='date_price_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 14, 42), verbose_name='date published'),
        ),
    ]
