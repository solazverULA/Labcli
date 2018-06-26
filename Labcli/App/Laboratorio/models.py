from django.db import models

# Create your models here.

from App.Paciente.models import Paciente
from App.examenes.models import Examenes

from django.db.models import Sum


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
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return 'Id Solicitud: {} Datos:{} {}  Pago: {} '.format(self.id, self.paciente.nombrepa,
                                                           self.paciente.apellidopa, self.pagado)

class ResultadoDat(models.Model):
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    solicitud  = models.ForeignKey(Solicitud, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.solicitud.pagado)


class Detalle_examen(models.Model):
    resultadodat = models.ForeignKey(ResultadoDat, null=True, blank=True, on_delete=models.CASCADE)
    examenes = models.ForeignKey(Examenes, null=True, blank=True, on_delete=models.CASCADE)
    valores=models.CharField(max_length=100)
    fecharesultado = models.DateField(auto_now_add=True, null=True, blank=True)
    validacion = models.BooleanField(default=False)


    def __str__(self):
        return '{} {} {} {} {}'.format(self.examenes.nombre, self.examenes.rango, self.resultadodat.paciente.nombrepa,
                             self.resultadodat.paciente.apellidopa, self.resultadodat.id)
