from django.db import models

from App.Paciente.models import Paciente
from App.examenes.models import Examenes


# Create your models here.


class Resultado(models.Model):
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)


class Detalle_examen(models.Model):
    resultado = models.ForeignKey(Resultado, null=True, on_delete = models.CASCADE)
    examenes = models.ForeignKey(Examenes, null=True, blank=True, on_delete=models.CASCADE)
    valores=models.CharField(max_length=100)

