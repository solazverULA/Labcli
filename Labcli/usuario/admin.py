# usuario/admin.py
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usuario.forms import (
    CustomUserChangeForm,
    CustomUserCreationForm
)
from usuario.models import (
    BioanalistaProfile,
    PacienteProfile,
    AsistenteProfile,
    User
)


# Heredamos del UserAdmin original para usar nuestros formularios customizados
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': (
                    'is_bioanalista',
                    'is_asistente',
                    'is_paciente'
                )
            }
        ),
    )


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    list_display =  (
        'id',
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        'is_bioanalista',
        'is_paciente',
        'is_asistente',
        'last_login',
        'date_joined'
    )


@admin.register(PacienteProfile)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'active',
        'user_id'
    )


@admin.register(BioanalistaProfile)
class BioanalistaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'active',
        'user_id'
    )
@admin.register(AsistenteProfile)
class AsistenteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'active',
        'user_id'
    )