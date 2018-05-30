from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

from App.Paciente.forms import PacienteForm
from App.Paciente.models import Paciente


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect



@login_required
def index(request):
    if not request.user.is_paciente:
        return HttpResponse("No tienes acceso a esta parte.")

    return render(request, 'templates/Paciente/index.html')



def Paciente_view(request):
    if not request.user.is_paciente:
        return HttpResponse("No tienes acceso a esta parte.")
    if request.method =='POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Paciente:index')

    else:
        form = PacienteForm()
    return render(request, 'templates/Paciente/paciente_form.html',{'form':form})

def Paciente_list(request):
    if not request.user.is_asistente:
        return HttpResponse("No tienes acceso a esta parte.")
    paciente = Paciente.objects.all().order_by('id')
    contexto = {'Pacientes':paciente}
    return render(request.user.get_paciente_profile(), 'templates/Paciente/paciente_list.html',contexto)

class PacienteList(ListView):
    model = Paciente
    template_name = 'templates/Paciente/paciente_list.html'
    paginate_by = 2

class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'templates/Paciente/paciente_form.html'
    success_url = reverse_lazy('Paciente:ver_lista')

class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'templates/Paciente/paciente_form.html'
    success_url = reverse_lazy('Paciente:ver_lista')

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = 'templates/Paciente/paciente_delete2.html'
    success_url = reverse_lazy('Paciente:ver_lista')