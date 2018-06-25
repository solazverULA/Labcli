from django.db import models

# Create your models here.

from App.Paciente.models import Paciente
from App.examenes.models import Examenes

#from __future__ import unicode_literals

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

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidopa)





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
    fecha_sol = models.DateField(help_text='Formato: 2018-01-01')
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    asistente = models.ForeignKey(Asistente, null=True, blank=True, on_delete=models.CASCADE)
    examenes = models.ManyToManyField(Examenes)

    def __str__(self):
        return '{} {}'.format(self.paciente.nombrepa, self.paciente.apellidopa)



class Pago(models.Model):
    modalidad = models.CharField(max_length=50)
    monto = models.IntegerField()
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)



class ResultadoDat(models.Model):
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.paciente.nombrepa, self.paciente.apellidopa)


class Detalle_examen(models.Model):
    resultadodat = models.ForeignKey(ResultadoDat, null=True, blank=True, on_delete=models.CASCADE)
    examenes = models.ForeignKey(Examenes, null=True, blank=True, on_delete=models.CASCADE)
    valores=models.CharField(max_length=100)

    def __str__(self):
        return '{}{}{}'.format(self.paciente.nombrepa, self.paciente.apellidopa, self.examenes.nombre, self.resultadodat.id)


class Resultado(models.Model):
    valores = models.CharField(max_length=50)
    examenes = models.ForeignKey(Examenes, null=True, blank=True, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    examen = models.ForeignKey(Detalle_examen, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.nombre)




class DetalleExamen(models.Model):
    list=models.ForeignKey(Resultado, null=True, blank=True, on_delete=models.CASCADE, related_name='resultado')
    examen=models.ForeignKey(Examenes, null=True, on_delete = models.CASCADE)
    valores=models.CharField(max_length=9)






# models.py
from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100)


class TodoItem(models.Model):
    name = models.CharField(max_length=150, help_text="e.g. Buy milk, wash dog etc")
    list = models.ForeignKey(TodoList, null=True, on_delete = models.CASCADE)


