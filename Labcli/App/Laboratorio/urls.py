from django.urls import path
from django.contrib.auth.decorators import login_required

from App.Laboratorio.views import index_lab

from App.Laboratorio.views import SolicitudCreate, SolicitudUpdate, SolicitudList, SolicitudDelete
from App.Laboratorio.views import Detalle_examenCreate, Detalle_examen_List
from App.Laboratorio.views import Detalle_examen_Delete, Detalle_examen_Update
app_name = 'App'

urlpatterns = [
    path('', index_lab, name= 'index'),
    path('NuevaSolicitud', login_required(SolicitudCreate.as_view()), name='crear_solicitud'),
    path('ListaSolicitud', login_required(SolicitudList.as_view()), name='ver_solicitud'),
    path('EditarSolicitud/<pk>', login_required(SolicitudUpdate.as_view()), name='editar_solicitud'),
    path('Eliminar/<pk>', SolicitudDelete.as_view(), name='eliminar_lista'),
    path('NuevoExamenValores2', login_required(Detalle_examenCreate.as_view()), name='crear_examenvalores2'),
    path('ListaResultadoExamen', login_required(Detalle_examen_List.as_view()), name='ver_resultados_examen'),
    path('EliminarResultadoExamen/<pk>', Detalle_examen_Delete.as_view(), name='eliminar_resultado_examen'),
    path('EditarResultadoExamen/<pk>', login_required(Detalle_examen_Update.as_view()), name='editar_resultado_examen'),

]


