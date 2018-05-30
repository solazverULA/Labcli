from django.contrib import admin

# Register your models here.

from App.Paciente.models import Paciente

admin.site.register(Paciente)