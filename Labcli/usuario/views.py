# Create your views here.

from django.http import HttpResponse
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


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
    success_url = reverse_lazy('Paciente:crear_paciente')





class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')