# Generated by Django 4.2 on 2024-07-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_height_alter_pokemon_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('A', 'Agua'), ('T', 'Tierra'), ('E', 'Eléctrico'), ('F', 'Fuego')], max_length=30),
        ),
    ]
