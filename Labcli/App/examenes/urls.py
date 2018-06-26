from django.urls import path, include


from django.contrib.auth.decorators import login_required
from App.examenes.views import ExamenCreate, index, ExamenList, ExamenUpdate, ExamenDelete

app_name = 'App'

urlpatterns = [
    path('', index, name='index'),
    path('Crear',login_required(ExamenCreate.as_view()), name='crear_examen'),
    path('ListaExamenes', login_required(ExamenList.as_view()), name='ver_lista'),
    path('EditarExamenes/<pk>', login_required(ExamenUpdate.as_view()), name='editar_examen'),
    path('EliminarExamenes/<pk>', ExamenDelete.as_view(), name='eliminar_examen'),

]