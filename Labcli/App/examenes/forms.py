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
            'stock',
        ]

        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo de examen',
            'precio': 'Precio de examen',
            'precio_laboratorio': 'Precio de laboratorio',
            'stock': 'stock',
        }


        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'precio_laboratorio': forms.TextInput(attrs={'class':'form-control'}),
            'stock': forms.TextInput(attrs={'class':'form-control'}),
         }