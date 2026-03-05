from django.contrib import admin
from .models import Vehiculos, Taxis, Conductores,TarjetaControls
# Register your models here.
admin.site.register(Vehiculos)
admin.site.register(Taxis)
admin.site.register(Conductores)
admin.site.register(TarjetaControls)