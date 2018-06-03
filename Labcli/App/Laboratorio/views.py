from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
# Create your views here.

from App.Laboratorio.forms import SolicitudForm
from App.Laboratorio.models import Solicitud

from App.Paciente.forms import PacienteForm
from App.Paciente.models import Paciente

from App.examenes.forms import ExamenForm


def index_lab(request):
    return HttpResponse("Laboratorio")


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'templates/Laboratorio/solicitud_list.html'


class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'templates/Laboratorio/solicitud_form.html'
    success_url = reverse_lazy('Laboratorio:ver_solicitud')

class SolicitudUpdate(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    second_form_class = PacienteForm
    second_model = Paciente
    template_name = 'templates/Laboratorio/solicitud_form.html'
    success_url = reverse_lazy('Laboratorio:ver_solicitud')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        paciente = self.second_model.objects.get(id=solicitud.paciente_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance= solicitud.paciente)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        paciente = self.second_model.objects.get(id=solicitud.paciente_id)
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=solicitud.paciente)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'templates/Laboratorio/solicitud_delete.html'
    success_url = reverse_lazy('Laboratorio:ver_solicitud')