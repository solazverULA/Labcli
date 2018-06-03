from django.shortcuts import render

from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from App.examenes.forms import ExamenForm

from App.examenes.models import Examenes
# Create your views here.

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.urls import reverse_lazy



@login_required
def index(request):
    if not request.user.is_paciente:
        return HttpResponse("No tienes acceso a esta parte.")

    return render(request, 'templates/Paciente/index.html')



class ExamenCreate(CreateView):
    model = Examenes
    form_class = ExamenForm
    template_name = 'templates/Examenes/examenes_form.html'
    success_url = reverse_lazy('Examenes:ver_lista')


class ExamenList(ListView):
    model = Examenes
    template_name = 'templates/Examenes/examenes_list.html'
    paginate_by = 2
