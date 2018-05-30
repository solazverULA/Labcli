# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
import json
from rest_framework.views import APIView

from usuario.forms import RegistroForm
from usuario.serializer import UserSerializer


class RegistroUsuario(CreateView):
    model = User
    template_name = "templates/usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('Paciente:ver_lista')


class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')