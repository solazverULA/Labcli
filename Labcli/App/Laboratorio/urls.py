from django.urls import path
from django.contrib.auth.decorators import login_required

from App.Laboratorio.views import index_lab

from App.Laboratorio.views import SolicitudCreate, SolicitudUpdate, SolicitudList
#SolicitudDelete
app_name = 'App'

urlpatterns = [
    path('', index_lab, name= 'index'),
    path('NuevaSolicitud', login_required(SolicitudCreate.as_view()), name='crear_solicitud'),
    path('ListaSolicitud', login_required(SolicitudList.as_view()), name='ver_solicitud'),
    path('EditarSolicitud/<pk>', login_required(SolicitudUpdate.as_view()), name='editar_solicitud'),
    #path('Eliminar/<pk>', SolicitudDelete.as_view(), name='eliminar_lista'),
]

