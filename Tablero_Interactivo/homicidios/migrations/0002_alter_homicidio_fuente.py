# Generated by Django 5.0.4 on 2024-11-12 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homicidios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homicidio',
            name='fuente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homicidios.fuente'),
        ),
    ]
