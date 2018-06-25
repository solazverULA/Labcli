from django import forms

from App.Laboratorio.models import Solicitud, Resultado
from App.Paciente.models import Paciente

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