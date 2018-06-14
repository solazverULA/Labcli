from django import forms

from App.Paciente.models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente

        fields = [
            'cedula',
            'nombrepa',
            'apellidopa',
            'apellidoma',
            'sexo',
            'fecha_nac',
            'telefono',
            'domicilio',
            'user',
        ]

        labels = {
            'cedula': 'CI',
            'nombrepa': 'Nombre',
            'apellidopa': 'Apellido Paterno',
            'apellidoma': 'Apellido Materno',
            'fecha_nac': 'Fecha nacimiento',
            'telefono': 'Telefono',
            'domicilio':'Domicilio',
            'user':'user,'
        }


        widgets = {
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombrepa': forms.TextInput(attrs={'class':'form-control'}),
            'apellidopa': forms.TextInput(attrs={'class':'form-control'}),
            'apellidoma': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),

        }


