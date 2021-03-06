from django import forms
from App.examenes.models import Examenes


class ExamenForm(forms.ModelForm):

    class Meta:
        model = Examenes

        fields = [
            'nombre',
            'tipo',
            'precio',
            'precio_laboratorio',
            'rango',
        ]

        labels = {
            'nombre': 'Nombre de Examen',
            'tipo': 'Tipo de examen',
            'precio': 'Precio de Examen',
            'precio_laboratorio': 'Valor de examen',
            'rango': 'Rango de examen'
        }


        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'precio_laboratorio': forms.TextInput(attrs={'class':'form-control'}),
            'rango': forms.TextInput(attrs={'class': 'form-control'}),

        }