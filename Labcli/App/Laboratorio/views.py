from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db import transaction
# Create your views here.

from App.Laboratorio.forms import SolicitudForm, ResultadoForm, ExamenVForm, TodoItem, TodoList, TodoItemForm, TodoListForm

from App.Laboratorio.forms import Detalle_examenFormSet, Detalle_examenForm
from App.Laboratorio.models import Solicitud, Resultado, Detalle_examen, ResultadoDat

from App.Paciente.forms import PacienteForm
from App.Paciente.models import Paciente

from App.examenes.forms import ExamenForm

from django.forms.formsets import formset_factory, BaseFormSet

def index_lab(request):
    return HttpResponse("Laboratorio")


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'templates/Laboratorio/solicitud_list.html'


class ExamenValorCreate(CreateView):
    model = Detalle_examen
    form_class = ExamenVForm
    template_name = 'templates/Laboratorio/examen_form.html'
    success_url = reverse_lazy('Laboratorio:ver_valores')


class ValorList(ListView):
    model = Detalle_examen
    template_name = 'templates/Laboratorio/examen_list.html'



class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'templates/Laboratorio/solicitud_form.html'
    success_url = reverse_lazy('Laboratorio:ver_solicitud')



class ResultadoCreate(CreateView):
    model = Resultado
    form_class = ResultadoForm
    template_name = 'templates/Laboratorio/resultado_form.html'
    success_url = reverse_lazy('Laboratorio:ver_resultado')


class ResultadoList(ListView):
    model = Resultado
    template_name = 'templates/Laboratorio/resultado_list.html'



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


class ResultadoDelete(DeleteView):
    model = Resultado
    template_name = 'templates/Laboratorio/resultado_delete.html'
    success_url = reverse_lazy('Laboratorio:ver_resultado')



class ResultadoUpdate(UpdateView):
    model = Resultado
    form_class = ResultadoForm
    second_form_class = PacienteForm
    second_model = Paciente
    template_name = 'templates/Laboratorio/resultado_form.html'
    success_url = reverse_lazy('Laboratorio:ver_resultado')




from django.shortcuts import render_to_response
from django.template import RequestContext  # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect



def index(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    TodoItemFormSet = formset_factory(TodoItemForm, max_num=10, formset=RequiredFormSet)
    if request.method == 'POST': # If the form has been submitted...
        todo_list_form = TodoListForm(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        todo_item_formset = TodoItemFormSet(request.POST, request.FILES)

        if todo_list_form.is_valid() and todo_item_formset.is_valid():
            todo_list = todo_list_form.save()
            for form in todo_item_formset.forms:
                todo_item = form.save(commit=False)
                todo_item.list = todo_list
                todo_item.save()
            return HttpResponseRedirect('thanks') # Redirect to a 'success' page
    else:
        todo_list_form = TodoListForm()
        todo_item_formset = TodoItemFormSet()



    return render_to_response('index.html')



class Detalle_examenCreate(CreateView):
    model = ResultadoDat
    fields = ['paciente']
    success_url = reverse_lazy('Laboratorio:ver_resultado')

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
