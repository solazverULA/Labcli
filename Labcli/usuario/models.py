# usuario/models.py
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.contenttypes.fields import GenericRelation

class User(AbstractUser):
    is_bioanalista = models.BooleanField(default=False)
    is_asistente = models.BooleanField(default=False)
    is_paciente = models.BooleanField(default=False)

    def get_bioanalista_profile(self):
        medical_profile = None
        if hasattr(self, 'medicalprofile'):
            bioanalista_profile = self.bioanalistaprofile
        return bioanalista_profile

    def get_asistente_profile(self):
        patient_profile = None
        if hasattr(self, 'patientprofile'):
            asistente_profile = self.asistenteprofile
        return asistente_profile

    def get_paciente_profile(self):
        paciente_profile = None
        if hasattr(self, 'pacienteprofile'):
            paciente_profile = self.get_paciente_profile()
        return paciente_profile

    class Meta:
        db_table = 'auth_user'

    @classmethod
    def get_by_id(cls, uid):
        return User.objects.get(pk=uid)

    def __unicode__(self):
        return self.email


class BioanalistaProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


class PacienteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.user.username)

class AsistenteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
