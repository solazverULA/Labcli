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
        ]

        labels = {
            'nombre': 'Nombre de Examen',
            'tipo': 'Tipo de examen',
            'precio': 'Valor de examen',
            'precio_laboratorio': 'Precio de Examen',
        }


        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'precio_laboratorio': forms.TextInput(attrs={'class':'form-control'}),
        }