from django.db import models

# Create your models here.

class Administradores(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    correo = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    def nombre_admin(self):
        return f"{self.nombres} {self.apellidos}"

class Vehiculos (models.Model):
    TIPO_CHOICES = [
        ('TAX','Taxi'),
        ('MIU','Microbus urbano'),
        ('CIT','Camioneta intermunicipal'),
        ('MIT','Microbus intermunicipal'),
    ]
    tipo_vehiculo = models.CharField(choices= TIPO_CHOICES, max_length=3, default='TAX')
    precio = models.CharField(max_length=20)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=20)
    capacidad = models.CharField(max_length=2)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo_vehiculo} - {self.marca} - {self.modelo}"
    def vehiculo_venta(self):
        return f"{self.tipo_vehiculo} - {self.marca} - {self.modelo}"
