from django import forms

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
            'email': 'Email',
            'telefono': 'Telefono',
            'domicilio':'Domicilio',
        }


        widgets = {
            'nombrepa': forms.TextInput(attrs={'class':'form-control'}),
            'apellidoma': forms.TextInput(attrs={'class':'form-control'}),
            'apellidopa': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
        }


