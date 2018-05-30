from django.contrib import admin

# Register your models here.

from App.Laboratorio.models import Bioanalista, Asistente, Solicitud, Muestra, Examen, Resultado, Pago

admin.site.register(Bioanalista)
admin.site.register(Asistente)
admin.site.register(Solicitud)
admin.site.register(Muestra)
admin.site.register(Examen)
admin.site.register(Resultado)
admin.site.register(Pago)