from django.db import models
from django.http import HttpResponse
from django.template import Template, context

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    horario = models.TimeField()
    def __str__(self):
        return f"{self.nombre} - {self.horario}"

class Alumno(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    clase_a_cargo = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
