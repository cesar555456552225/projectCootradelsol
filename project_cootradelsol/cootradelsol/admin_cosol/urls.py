from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('saludo/', views.home, name='saludo'),
    path('vehiculos_venta/', views.vehiculos_venta, name='vehiculos_venta' ),
    path('vehiculos_venta/<int:id>/', views.detalle_vehiculo_venta, name='detalle_vehiculo_venta'),
    path('eliminar_vehiculo/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('crear_vehiculo_venta/', views.crear_vehiculo_venta, name= 'crear_vehiculo_venta'),
    path('asociados/', views.asociados, name='asociados'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agregar_conductor/', views.agregar_conductor, name='agregar_conductor'),
    path('crear_taxi/', views.crear_taxi, name='crear_taxi'),
    path('crear_tarjeta_control/', views.crear_tarjeta_control, name='crear_tarjeta_control'),
    path('lista_taxis/', views.lista_taxis, name='lista_taxis'),
    path('lista_conductores/', views.lista_conductores, name='lista_conductores'),
    path('lista_tarjeta_control/', views.lista_tarjeta_control, name='lista_tarjeta_control'),
]