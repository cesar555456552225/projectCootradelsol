from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Vehiculos
from .forms import VehiculoForm
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

def vehiculos(request):
    vehiculos = Vehiculos.objects.all()
    return render(request, 'vehiculos.html',{
        'vehiculos':vehiculos
    })

def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculos, id=id)
    return render(request, 'detalle_vehiculo.html',{
        'vehiculo':vehiculo
    })

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehiculos')
        else:
            form = VehiculoForm()
        return render(request, 'crear_vehiculo.html', {'form':form})
    return render(request, 'crear_vehiculo.html', {'form': VehiculoForm()})

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
        return redirect('vehiculos')
    return redirect('vehiculos')

def asociados(request):
    template = loader.get_template('asociados.html')
    return HttpResponse(template.render())