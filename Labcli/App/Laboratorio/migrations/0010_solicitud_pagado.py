# Generated by Django 2.0.5 on 2018-06-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratorio', '0009_auto_20180625_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
    ]