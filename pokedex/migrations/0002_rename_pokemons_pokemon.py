# Generated by Django 4.2 on 2024-07-06 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pokemons',
            new_name='Pokemon',
        ),
    ]
