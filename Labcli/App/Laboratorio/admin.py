from django.contrib import admin

# Register your models here.

from App.Laboratorio.models import Bioanalista, Asistente, Solicitud, Detalle_examen, Resultado, Pago, DetalleExamen
from App.Laboratorio.models import TodoItem, TodoList

admin.site.register(Bioanalista)
admin.site.register(Asistente)
admin.site.register(Solicitud)
#admin.site.register(Resultado)
admin.site.register(Pago)
admin.site.register(Detalle_examen)


admin.site.register(TodoItem)


class examen_valoresInline(admin.TabularInline):
    model = DetalleExamen

class examenAdminInline(admin.ModelAdmin):
    inlines = (examen_valoresInline,)

admin.site.register(Resultado, examenAdminInline)


class TodoItemAdmin(admin.TabularInline):
    model = TodoItem
    extra = 0

class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoItemAdmin]

admin.site.register(TodoList, TodoListAdmin)