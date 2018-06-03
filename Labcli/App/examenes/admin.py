from django.contrib import admin
from App.examenes.models import Examenes
# Register your models here.

class ExamenesAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'precio','precio_laboratorio', 'stock')
	search_fields = ('nombre', 'tipo')

admin.site.register(Examenes,ExamenesAdmin)
