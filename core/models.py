from django.db import models
from django.db.models.base import Model

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Guitarra(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo_cuerpo = models.CharField(max_length=50)
    tipo_guitarra = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="guitarra", null=True)

    def __str__(self):
        return self.marca

class Bajo(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo_cuerpo = models.CharField(max_length=50)
    tipo_bajo = models.CharField(max_length=50)
    cantidad_cuerda = models.IntegerField()
    valor = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="bajo", null=True)

    def __str__(self):
        return self.marca

class Piano(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo_piano = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="piano", null=True)

    def __str__(self):
        return self.marca

class Percusion(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo_bateria = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="percusion", null=True)

    def __str__(self):
        return self.marca

class Amplificador(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo_amplificador = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="amplificador", null=True)

    def __str__(self):
        return self.marca

class Accesorio(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    tipo_accesorio = models.CharField(max_length=50)
    nombre_accesorio = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="accesorio", null=True)

    def __str__(self):
        return self.marca


opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]
class Contacto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre









   

