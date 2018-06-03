"""Labcli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('admin/', admin.site.urls),
    path('examenes/', include('App.examenes.urls', namespace="Examenes")),
    path('Paciente/', include('App.Paciente.urls', namespace='Paciente')),
    path('Laboratorio/', include('App.Laboratorio.urls', namespace='Laboratorio')),
    path('usuario/', include('usuario.urls', namespace='usuario')),
    path('accounts/login/', login, {'template_name':'index.html'}, name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('reset/password_reset', password_reset,
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'templates/registration/password_reset_email.html'},
        name='password_reset'),
    path('password_reset_done', password_reset_done,
        {'template_name': 'templates/registration/password_reset_done.html'},
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
        {'template_name': 'templates/registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    path('reset/done', password_reset_complete, {'template_name': 'templates/registration/password_reset_complete.html'},
    name='password_reset_complete'),
]


