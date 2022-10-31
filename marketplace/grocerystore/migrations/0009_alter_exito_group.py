# Generated by Django 4.1 on 2022-10-31 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0008_alter_exito_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exito',
            name='group',
            field=models.CharField(choices=[('F', 'Food'), ('C', 'Cleaning'), ('V', 'Vegetables')], max_length=1),
        ),
    ]