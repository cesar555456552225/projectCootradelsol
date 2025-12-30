from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('saludo/', views.home, name='saludo'),
    path('vehiculos/', views.detalle_vehiculos, name='vehiculos' )
]