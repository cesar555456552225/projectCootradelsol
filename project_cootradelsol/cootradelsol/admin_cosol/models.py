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
        ('Taxi','Taxi'),
        ('Microbus Urbano','Microbus urbano'),
        ('Camioneta intermunicipal','Camioneta intermunicipal'),
        ('Microbus intermunicipal','Microbus intermunicipal'),
    ]
    tipo_vehiculo = models.CharField(choices= TIPO_CHOICES, max_length=50, default='TAX')
    precio = models.CharField(max_length=20)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=20)
    capacidad = models.CharField(max_length=2)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField( upload_to='vehiculos/',blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo_vehiculo} - {self.marca} - {self.modelo}"
    def vehiculo_venta(self):
        return f"{self.tipo_vehiculo} - {self.marca} - {self.modelo}"

class Taxis (models.Model):
    numero_interno = models.IntegerField(max_length=3)
    placa = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    modelo = models.IntegerField(max_length=4)
    radio = models.CharField(max_length=20)
    marca_radio = models.CharField(max_length=20)
    soat = models.DateField(blank=True, null=True)
    tecnomicanica = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.numero_interno} - {self.placa}"

class Conductores(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    numero_identificacion = models.CharField(max_length=20)
    rh = models.CharField(max_length=3)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    eps = models.CharField(max_length=50)
    arl = models.CharField(max_length=50)
    anotaciones = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='conductores/', blank=True, null=True)
    taxi = models.ForeignKey(Taxis, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.taxi}"
