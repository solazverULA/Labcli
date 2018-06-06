from django.urls import path
from django.contrib.auth.decorators import login_required

from App.Laboratorio.views import index_lab

from App.Laboratorio.views import SolicitudCreate, SolicitudUpdate, SolicitudList, SolicitudDelete
from App.Laboratorio.views import  ResultadoCreate, ResultadoList, ResultadoDelete, ResultadoUpdate


app_name = 'App'

urlpatterns = [
    path('', index_lab, name= 'index'),
    path('NuevaSolicitud', login_required(SolicitudCreate.as_view()), name='crear_solicitud'),
    path('ListaSolicitud', login_required(SolicitudList.as_view()), name='ver_solicitud'),
    path('EditarSolicitud/<pk>', login_required(SolicitudUpdate.as_view()), name='editar_solicitud'),
    path('Eliminar/<pk>', SolicitudDelete.as_view(), name='eliminar_lista'),
    path('NuevoResultado', login_required(ResultadoCreate.as_view()), name='crear_resultado'),
    path('ListaResultado', login_required(ResultadoList.as_view()), name='ver_resultado'),
    path('EliminarResultado/<pk>', ResultadoDelete.as_view(), name='eliminar_resultado'),
    path('EditarResultado/<pk>', login_required(ResultadoUpdate.as_view()), name='editar_resultado'),

]


