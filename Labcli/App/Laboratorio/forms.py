from django import forms
from django.forms import ModelForm
from django.forms import formset_factory, inlineformset_factory
from django.forms import ModelForm


from App.Laboratorio.models import Solicitud, Resultado, Detalle_examen, DetalleExamen, TodoList, TodoItem, ResultadoDat
from App.Paciente.models import Paciente
from App.examenes.models import Examenes
from App.Laboratorio.models import ResultadoDat

from django.forms.models import inlineformset_factory
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud


        fields = [
        'fecha_sol',
        'paciente',
        'examenes',
        ]

        labels = {
            'fecha_sol': 'Fecha Solicitud',
            'paciente': 'Paciente',
            'examenes': 'Examen',
            }



        widgets = {
            'fecha_sol': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class':'form-control'}),
            'examenes': forms.CheckboxSelectMultiple(),
            }



class ExamenVForm(forms.ModelForm):
    class Meta:
        model = Detalle_examen

        fields = [
            'examenes',
            'valores',
        ]

        labels = {
            'examenes':'examen',
            'valores':'valores1',
        }

        widgets = {
            'examenes': forms.Select(attrs={'class':'form-control'}),
            'valores': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado


        fields = [
        'valores',
        'examen',
        'paciente',
        ]

        labels = {
            'valores': 'Valores',
            'examen': 'Examen',
            'paciente':'Paciente'

        }

        widgets = {
            'valores': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'examen': forms.Select(attrs={'class':'form-control'}),
        }




#from dynamicform


class TodoListForm(ModelForm):
  class Meta:
      model = TodoList
      fields = [
          'name',
      ]


class TodoItemForm(ModelForm):
  class Meta:
    model = TodoItem
    fields = [
        'name',
    ]





class ResultadoDatForm(ModelForm):
    class Meta:
        model = ResultadoDat
        exclude = ()




class Detalle_examenForm(ModelForm):
    class Meta:
        model = Detalle_examen
        exclude = ()



Detalle_examenFormSet = inlineformset_factory(ResultadoDat, Detalle_examen, form=Detalle_examenForm, extra=3)
