# Generated by Django 5.1.7 on 2025-03-17 22:23

import gestion.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_galeria_alter_platillo_imagen_alter_promocion_ruta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=gestion.models.upload_to_galeria),
        ),
    ]
