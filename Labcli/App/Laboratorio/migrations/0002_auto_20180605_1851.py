# Generated by Django 2.0.5 on 2018-06-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultado',
            old_name='nombre',
            new_name='valores',
        ),
        migrations.AddField(
            model_name='resultado',
            name='solicitud',
            field=models.ManyToManyField(to='Laboratorio.Solicitud'),
        ),
    ]
