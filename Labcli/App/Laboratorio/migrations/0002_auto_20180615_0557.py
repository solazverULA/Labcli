# Generated by Django 2.0.5 on 2018-06-15 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Paciente', '0001_initial'),
        ('Laboratorio', '0001_initial'),
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='resultado',
            name='examen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Laboratorio.Detalle_examen'),
        ),
        migrations.AddField(
            model_name='resultado',
            name='examenes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examenes.Examenes'),
        ),
        migrations.AddField(
            model_name='resultado',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='pago',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='detalle_examen',
            name='examen',
            field=models.ManyToManyField(to='examenes.Examenes'),
        ),
    ]
