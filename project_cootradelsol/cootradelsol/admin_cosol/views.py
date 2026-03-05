from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Vehiculos
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
    template = loader.get_template('asociados.html')
    return HttpResponse(template.render())

def agregar_conductor(request):
    if request.method == 'POST':
        form = ConductorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('conductores')
        else:
            form = ConductorForm()
        return render (request, 'agregar_conductor.html', {'form':form})
    return render (request, 'agregar_conductor.html', {'form': ConductorForm()})

def crear_taxi(request):
    if request.method == 'POST':
        form = TaxiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('taxis')
        else:
            form = TaxiForm()
        return render(request, 'crear_taxi.html', {'form':form})
    return render(request, 'crear_taxi.html', {'form': TaxiForm()})

def crear_tarjeta_control(request):
    if request.method == 'POST':
        form = TarjetaControlForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tarjeta_controls')
        else:
            form = TarjetaControlForm()
            return render(request, 'crear_tarjeta_control.html', {'form':form})
    return render(request, 'crear_tarjeta_control.html', {'form': TarjetaControlForm()})

def lista_taxis(request):
    template = loader.get_template('lista_taxis.html')
    return HttpResponse(template.render())

def lista_conductores(request):
    template = loader.get_template('lista_conductores.html')
    return HttpResponse(template.render())

def lista_tarjeta_control(request):
    template = loader.get_template('tarjetas_control.html')
    return HttpResponse(template.render())