# Generated by Django 4.2 on 2024-07-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('T', 'Tierra'), ('F', 'Fuego'), ('A', 'Agua'), ('E', 'Eléctrico')], max_length=30),
        ),
    ]
