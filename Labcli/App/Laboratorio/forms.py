from django import forms

from App.Laboratorio.models import Solicitud
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
        'nombre',
        'fecha_sol',
        ]

        labels = {
            'nombre': 'Nombre de examen',
            'fecha_sol': 'Fecha Solicitud',
            }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_sol': forms.TextInput(attrs={'class': 'form-control'}),
            }