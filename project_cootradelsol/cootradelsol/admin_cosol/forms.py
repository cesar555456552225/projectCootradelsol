from django import forms
from .models import Administradores, Vehiculos

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['tipo_vehiculo', 'precio', 'marca', 'modelo', 'capacidad', 'descripcion', 'imagen']



