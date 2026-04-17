from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Vehiculos, Taxis, Conductores, TarjetaControls
from .forms import VehiculoForm, ConductorForm, TaxiForm, TarjetaControlForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
# Create your views here.

def home (request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def vehiculos_venta(request):
    vehiculos = Vehiculos.objects.all()
    return render(request, 'vehiculos_venta.html',{
        'vehiculos':vehiculos
    })

def detalle_vehiculo_venta(request, id):
    vehiculo = get_object_or_404(Vehiculos, id=id)
    return render(request, 'detalle_vehiculo_venta.html',{
        'vehiculo':vehiculo
    })

def crear_vehiculo_venta(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehiculos_venta')
        else:
            form = VehiculoForm()
        return render(request, 'crear_vehiculo_venta.html', {'form':form})
    return render(request, 'crear_vehiculo_venta.html', {'form': VehiculoForm()})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            return render(request, 'login.html', {
                'error' : 'Usuario o contraseña incorrectos'
                })
    return render(request, 'login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html')

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculos, id=id)

    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculos_venta')
    return redirect('vehiculos_venta')

def asociados(request):
    return render(request, 'asociados.html')

def agregar_conductor(request):
    if request.method == 'POST':
        form = ConductorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_conductores')
        else:
            form = ConductorForm()
        return render (request, 'agregar_conductor.html', {'form':form})
    return render (request, 'agregar_conductor.html', {'form': ConductorForm()})

def editar_conductor(request, id):
    conductor = get_object_or_404(Conductores, id=id)
    if request.method == 'POST':
        form = ConductorForm(request.POST, request.FILES, instance=conductor)
        if form.is_valid():
            form.save()
            return redirect('lista_conductores')
        else:
            form = ConductorForm(instance=conductor)
    return render (request, 'agregar_conductor.html', {'form': ConductorForm(), 'conductor': conductor})

def detalle_conductor(request, id):
    conductor = get_object_or_404(Conductores, id=id)
    return render(request, 'detalle_conductor.html', {'conductor': conductor})

from django.db.models import Q

def buscar_conductor(request):
    query = request.GET.get('q')
    conductores = Conductores.objects.filter((Q(nombre__icontains=query) | Q(cedula__icontains=query)))
    return render(request, 'buscar_conductor.html', {'conductores': conductores, 'query': query})

def crear_taxi(request):
    if request.method == 'POST':
        form = TaxiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_taxis')
        else:
            form = TaxiForm()
        return render(request, 'crear_taxi.html', {'form':form})
    return render(request, 'crear_taxi.html', {'form': TaxiForm()})

def editar_taxi(request, id):
    taxi = get_object_or_404(Taxis, id=id)
    if request.method == 'POST':
        form = TaxiForm(request.POST, request.FILES, instance=taxi)
        if form.is_valid():
            form.save()
            return redirect('lista_taxis')
        else:
            form = TaxiForm(instance=taxi)
    return render(request, 'crear_taxi.html', {'form': TaxiForm(), 'taxi': taxi})

def crear_tarjeta_control(request):
    if request.method == 'POST':
        form = TarjetaControlForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tarjetas_control')
        else:
            form = TarjetaControlForm()
            return render(request, 'crear_tarjeta_control.html', {'form':form})
    return render(request, 'crear_tarjeta_control.html', {'form': TarjetaControlForm()})

def editar_tarjeta(request, id):
    tarjeta_control = get_object_or_404(TarjetaControls, id=id)
    if request.method == 'POST':
        form = TarjetaControlForm(request.POST, request.FILES, instance=tarjeta_control)
        if form.is_valid():
            form.save()
            return redirect('tarjetas_control')
        else:
            form = TarjetaControlForm(instance=tarjeta_control)
    return render(request, 'crear_tarjeta_control.html', {'form': TarjetaControlForm(), 'tarjeta_control': tarjeta_control})

def lista_taxis(request):
    taxis = Taxis.objects.all()
    return render(request, 'lista_taxis.html', {'taxis':taxis})

def lista_conductores(request):
    conductores = Conductores.objects.all()
    return render(request, 'lista_conductores.html', {'conductores': conductores})

def lista_tarjeta_control(request):
    tarjetas_control = TarjetaControls.objects.all()
    return render(request, 'tarjetas_control.html', {'tarjetas_control': tarjetas_control})