# Generated by Django 4.2 on 2024-07-13 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('T', 'Tierra'), ('A', 'Agua'), ('F', 'Fuego'), ('E', 'Eléctrico')], max_length=30),
        ),
    ]
