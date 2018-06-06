from django import forms

from App.Laboratorio.models import Solicitud, Resultado
from App.Paciente.models import Paciente



class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente

        fields = [
            'nombrepa',
            'apellidoma',
            'apellidopa',
            'sexo',
            'fecha_nac',
            'edad',
            'email',
            'telefono',
            'domicilio',
        ]

        labels = {
            'nombrepa': 'Nombre',
            'apellidoma': 'Apellido Materno',
            'apellidopa': 'Apellido Paterno',
            'sexo': 'Sexo',
            'fecha_nac': 'Fecha nacimiento',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }


        widgets = {
            'nombrepa': forms.TextInput(attrs={'class':'form-control'}),
            'apellidoma': forms.TextInput(attrs={'class':'form-control'}),
            'apellidopa': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control'}),
        }


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
            'examenes': 'Examen'
            }



        widgets = {
            'fecha_sol': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class':'form-control'}),
            'examenes':forms.CheckboxSelectMultiple(),
            }




class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado


        fields = [
        'valores',
        'examenes',
        'paciente',
        ]

        labels = {
            'valores': 'Valores',
            'examenes': 'Examen',
            'paciente':'Paciente'

        }

        widgets = {
            'valores': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'examenes': forms.Select(attrs={'class':'form-control'}),
        }