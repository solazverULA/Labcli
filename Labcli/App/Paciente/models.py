from django.db import models

#from App.Laboratorio.models import Muestra
# Create your models here.
from django.db.models import signals


class Paciente(models.Model):
#    idPaciente = models(primary_key=True)
    #idcedula = models.CharField(max_length=9, unique=True, null=False, blank=False)

    nombrepa = models.CharField(max_length=50)
    apellidoma = models.CharField(max_length=50)
    apellidopa = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    fecha_nac = models.DateField()
    edad = models.IntegerField()
    email = models.TextField()
    telefono = 	models.CharField(max_length=12)
    domicilio = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombrepa, self.apellidoma)