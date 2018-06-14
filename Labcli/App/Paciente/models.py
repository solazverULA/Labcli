from django.db import models
from django.db.models import signals

from django.core.validators import RegexValidator
from django.contrib.contenttypes.fields import GenericRelation

from usuario.models import User, PacienteProfile

from django.shortcuts import render

#import datatime

# Create your models here.

Sexo = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)



class Paciente(models.Model):
    cedula = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(regex="^[V|E][0-9]{7,9}$",
                           message="Formato de cédula inválido , ej: V0123456")],
        help_text='Formato: V012345678',)

    nombrepa = models.CharField(max_length=30)
    apellidopa = models.CharField(max_length=30)
    apellidoma = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=Sexo)
    fecha_nac = models.DateField( help_text='Formato: 2018-01-01')
    telefono = models.PositiveIntegerField()
    domicilio = models.TextField()
    user  = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombrepa, self.apellidopa, self.user.username)


   # def edad(self):
   #     return int((datetime.now().date() - self.fechanaciomiento).days / 365.25)
