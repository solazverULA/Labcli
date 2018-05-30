from django.db import models

# Create your models here.

from App.Paciente.models import Paciente


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
    nombre = models.CharField(max_length=50)
    fecha_sol = models.DateField()
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    asistente = models.ForeignKey(Asistente, null=True, blank=True, on_delete=models.CASCADE)

class Pago(models.Model):
    modalidad = models.CharField(max_length=50)
    monto = models.IntegerField()
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Examen(models.Model):
    nombre = models.CharField(max_length=50)
#    resultado = models.ManyToManyField(Resultado)



class Resultado(models.Model):
    nombre = models.CharField(max_length=50)
    examen = models.ManyToManyField(Examen)



class Muestra(models.Model):
    nombre = models.CharField(max_length=50)