from django.contrib import admin

# Register your models here.

from App.Laboratorio.models import Bioanalista, Asistente, Solicitud, Detalle_examen, ResultadoDat


admin.site.register(Bioanalista)
admin.site.register(Asistente)
admin.site.register(Solicitud)
admin.site.register(Detalle_examen)
admin.site.register(ResultadoDat)

