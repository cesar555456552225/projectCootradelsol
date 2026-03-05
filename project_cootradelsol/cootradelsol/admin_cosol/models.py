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
    
    def taxicosol (self):
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
    
    def conductorinfo(self):
        return f"{self.nombres} {self.apellidos} - {self.taxi}"

class TarjetaControls (models.Model):
    numero_tarjeta = models.CharField(max_length=10)
    fecha_expedicion = models.DateField(blank=True, null=True)
    conductor = models.ForeignKey(Conductores, on_delete=models.CASCADE)
    taxi = models.ForeignKey(Taxis, on_delete=models.CASCADE)
    refrendada1 = models.DateField(blank=True, null=True, verbose_name="Refrendada 1")
    vencimientorefrendada1 = models.DateField(blank=True, null=True, verbose_name="vencimiento refrendad 1")
    refrendada2 = models.DateField(blank=True, null=True, verbose_name="Refrendada 2")
    vencimientorefrendada2 = models.DateField(blank=True, null=True, verbose_name="vencimiento refrendada 2")
    refrendada3 = models.DateField(blank=True, null=True, verbose_name="Refrendada 3")
    vencimientorefrendada3 = models.DateField(blank=True, null=True, verbose_name="vencimiento refrendada 3")
    refrendada4 = models.DateField(blank=True, null=True, verbose_name="Refrendada 4")
    vencimientorefrendada4 = models.DateField(blank=True, null=True, verbose_name="vencimiento refrendada 4")
    refrendada5 = models.DateField(blank=True, null=True, verbose_name="Refrendada 5")
    vencimientorefrendada5 = models.DateField(blank=True, null=True, verbose_name="vencimiento refrendada 5")
    refrendada6 = models.DateField(blank=True, null=True, verbose_name="Refrendada 6")
    vencimientorefrendada6 = models.DateField(blank=True, null=True, verbose_name="vencimiento refrendada 6")
    refrendada7 = models.DateField(blank=True, null=True, verbose_name="Refrendada 7")
    vencimientorefrendada7 = models.DateField(blank=True, null=True, verbose_name="vencimiento refrendada 7")

    def __str__(self):
        return f"{self.numero_tarjeta} - {self.taxi} - {self.conductor}"
    
    def tarjeta_info(self):
        return f"{self.numero_tarjeta} - {self.taxi} - {self.conductor}"