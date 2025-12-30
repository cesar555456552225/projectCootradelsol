from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home (request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def detalle_vehiculos (request):
    template = loader.get_template('vehiculos.html')
    return HttpResponse(template.render())