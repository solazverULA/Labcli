from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db import transaction
# Create your views here.

from django.shortcuts import render
from django.db.models import Sum

from App.Laboratorio.forms import SolicitudForm
from App.Laboratorio.forms import Detalle_examenFormSet, Detalle_examenForm

from App.Laboratorio.models import Solicitud, Detalle_examen, ResultadoDat

from App.Paciente.forms import PacienteForm
from App.Paciente.models import Paciente

from App.examenes.forms import ExamenForm

from django.forms.formsets import formset_factory, BaseFormSet

from django.template.response import TemplateResponse

def index_lab(request):
    return HttpResponse("Laboratorio")



#Solicitud Examen
#Solicitud Examen



class SolicitudList(ListView):
    model = Solicitud
    template_name = 'templates/Laboratorio/solicitud_list.html'


class SolicitudCreate(CreateView):
    model = Solicitud
  #  Solicitud.objects.all().aggregate(Sum('Solicitud.examenes.precio_lab'))
# Solicitud.objects.aggregate(Sum('examenes'))
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



class SolicitudUpdate2(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'templates/Laboratorio/solicitud_form.html'
    success_url = reverse_lazy('Laboratorio:ver_solicitud')



# Resultado Examenes
# Resultado Examenes
class Detalle_examenCreate(CreateView):
    model = ResultadoDat
    fields = ['paciente','solicitud']
    success_url = reverse_lazy('Laboratorio:ver_resultados_examen')

    def get_context_data(self, **kwargs):
        data = super(Detalle_examenCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['Detalle_examen'] = Detalle_examenFormSet(self.request.POST)
        else:
            data['Detalle_examen'] = Detalle_examenFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        Detalle_examen = context['Detalle_examen']
        with transaction.atomic():
            self.object = form.save()

            if Detalle_examen.is_valid():
                Detalle_examen.instance = self.object
                Detalle_examen.save()
        return super(Detalle_examenCreate, self).form_valid(form)

    template_name = 'templates/Laboratorio/detalle_examen.html'


class Detalle_examen_List(ListView):
    model = Detalle_examen
    template_name = 'templates/Laboratorio/resultado_list_examenes.html'


class Detalle_examen_Update(UpdateView):
    model = Detalle_examen
    form_class = Detalle_examenForm
    template_name = 'templates/Laboratorio/detalle_examen.html'
    success_url = reverse_lazy('Laboratorio:ver_resultados_examen')

class Detalle_examen_Delete(DeleteView):
    model = Detalle_examen
    template_name = 'templates/Laboratorio/resultado_examen_delete.html'
    success_url = reverse_lazy('Laboratorio:ver_resultados_examen')


def index2(request):
    obj = Detalle_examen.objects.filter(resultadodat__paciente__user=request.user).order_by('-fecharesultado')
    context = {
        "obj": obj,
       }
    return render(request, "templates/Laboratorio/consulta2.html", context)
