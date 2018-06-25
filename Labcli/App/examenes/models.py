from django.db import models
from django.db.models import signals

from App.Paciente.models import Paciente


# Create your models here.

class Examenes(models.Model):

	TIPO = (
        ('hematologia', 'Hematologia'),
        ('orina', 'Orina'),
    )

	nombre = models.CharField(max_length=200, unique=True)
	tipo = models.CharField(choices=TIPO, max_length=30)
	precio = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	precio_laboratorio = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return '{}'.format(self.nombre)