#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.forms import UserCreationForm



class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo',
        }


# usuario/forms.py
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm
)

from usuario.models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User