from django import forms
from .models import Administradores, Vehiculos, Conductores, TarjetaControls, Taxis

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['tipo_vehiculo', 'precio', 'marca', 'modelo', 'capacidad', 'descripcion', 'imagen']

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductores
        fields = ['nombres', 'apellidos', 'numero_identificacion', 'rh', 'direccion', 'telefono', 'eps', 'arl', 'anotaciones', 'taxi', 'imagen']

class TaxiForm(forms.ModelForm):
    class Meta:
        model = Taxis
        fields = ['numero_interno', 'placa', 'marca', 'modelo', 'radio', 'marca_radio', 'soat', 'tecnomicanica']

class TarjetaControlForm(forms.ModelForm):
    class Meta:
        model = TarjetaControls
        fields = ['numero_tarjeta', 'fecha_expedicion', 'conductor', 'taxi', 'refrendada1', 'vencimientorefrendada1', 'refrendada2', 'vencimientorefrendada2', 'refrendada3', 'vencimientorefrendada3', 'refrendada4', 'vencimientorefrendada4', 'refrendada5', 'vencimientorefrendada5', 'refrendada6', 'vencimientorefrendada6', 'refrendada7', 'vencimientorefrendada7']
