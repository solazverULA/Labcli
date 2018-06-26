from django import forms
from django.forms import ModelForm
from django.forms import formset_factory, inlineformset_factory
from django.forms import ModelForm


from App.Laboratorio.models import Solicitud, Detalle_examen, ResultadoDat
from App.Paciente.models import Paciente
from App.examenes.models import Examenes

from django.forms.models import inlineformset_factory

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud


        fields = [
        'fecha_sol',
        'paciente',
        'examenes',
        'pagado',
        ]

        labels = {
            'fecha_sol': 'Fecha Solicitud',
            'paciente': 'Paciente',
            'examenes': 'Examen',
            'pagado': 'Pagado'

            }



        widgets = {
            'fecha_sol': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class':'form-control'}),
            'examenes': forms.CheckboxSelectMultiple(),
        }


class ResultadoDatForm(ModelForm):
    class Meta:
        model = ResultadoDat
        exclude = ()




class Detalle_examenForm(ModelForm):
    class Meta:
        model = Detalle_examen
        exclude = ()



Detalle_examenFormSet = inlineformset_factory(ResultadoDat, Detalle_examen, form=Detalle_examenForm, extra=10)
