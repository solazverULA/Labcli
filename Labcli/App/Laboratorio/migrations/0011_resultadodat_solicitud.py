# Generated by Django 2.0.5 on 2018-06-26 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratorio', '0010_solicitud_pagado'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadodat',
            name='solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laboratorio.Solicitud'),
        ),
    ]