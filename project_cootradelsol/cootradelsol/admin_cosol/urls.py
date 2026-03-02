from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('saludo/', views.home, name='saludo'),
    path('vehiculos/', views.vehiculos, name='vehiculos' ),
    path('vehiculos/<int:id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('eliminar_vehiculo/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('crear_vehiculo/', views.crear_vehiculo, name= 'crear_vehiculo'),
    path('asociados/', views.asociados, name='asociados'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]