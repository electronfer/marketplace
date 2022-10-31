# Generated by Django 4.1 on 2022-10-31 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0005_exito_group_alter_exito_date_price_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exito',
            name='group',
            field=models.CharField(choices=[('FOOD', 'Food'), ('CLEANING', 'Cleaning'), ('VEGETABLES', 'Vegetables')], max_length=20, unique=True),
        ),
    ]
