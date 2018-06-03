# Generated by Django 2.0.5 on 2018-06-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrepa', models.CharField(max_length=50)),
                ('apellidoma', models.CharField(max_length=50)),
                ('apellidopa', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('fecha_nac', models.DateField()),
                ('edad', models.IntegerField()),
                ('email', models.TextField()),
                ('telefono', models.CharField(max_length=12)),
                ('domicilio', models.TextField()),
            ],
        ),
    ]
