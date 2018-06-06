from django.db import models

# Create your models here.

from App.Paciente.models import Paciente
from App.examenes.models import Examenes

class Bioanalista(models.Model):
   # IdBioanalista = models.CharField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoma = models.CharField(max_length=50)
    apellidopa = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    fecha_nac = models.DateField()
    edad = models.IntegerField()
    email = models.TextField()
    telefono = 	models.CharField(max_length=12)
    domicilio = models.TextField()



class Asistente(models.Model):
    #IdAsistente = models.CharField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoma = models.CharField(max_length=50)
    apellidopa = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    fecha_nac = models.DateField()
    edad = models.IntegerField()
    email = models.TextField()
    telefono = 	models.CharField(max_length=12)
    domicilio = models.TextField()


class Solicitud(models.Model):
    fecha_sol = models.DateField()
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    asistente = models.ForeignKey(Asistente, null=True, blank=True, on_delete=models.CASCADE)
    examenes = models.ManyToManyField(Examenes)


class Pago(models.Model):
    modalidad = models.CharField(max_length=50)
    monto = models.IntegerField()
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

class Examen(models.Model):
    nombre = models.CharField(max_length=50)
#    resultado = models.ManyToManyField(Resultado)



class Resultado(models.Model):
    valores = models.CharField(max_length=50)
    examen = models.ManyToManyField(Examen)
    examenes = models.ForeignKey(Examenes, null=True, blank=True, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)


class Muestra(models.Model):
    nombre = models.CharField(max_length=50)

