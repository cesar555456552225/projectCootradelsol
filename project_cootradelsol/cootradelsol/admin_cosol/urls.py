from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('saludo/', views.home, name='saludo')
]