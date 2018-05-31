from django.urls import path

from home.views import home, examenes, servicios

app_name = 'App'

urlpatterns = [
    path('', home, name='home'),
    path('Examenes', examenes, name='examenes'),
    path('Servicios', servicios, name='servicios'),
]
# Create your models here.
