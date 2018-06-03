from django.urls import path, include


from django.contrib.auth.decorators import login_required
from App.examenes.views import ExamenCreate, index, ExamenList

app_name = 'App'

urlpatterns = [
    path('', index, name='index'),
    path('Crear',login_required(ExamenCreate.as_view()), name='crear_examen'),
    path('ListaExamenes', login_required(ExamenList.as_view()), name='ver_lista'),

]