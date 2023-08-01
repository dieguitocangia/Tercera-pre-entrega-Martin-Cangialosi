from django.shortcuts import render
from django.http import HttpResponse
from .views import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'appDiego/base.html')

def clases(request):
    ctx = {"clases": Clase.objects.all()}
    return render(request, 'appDiego/clases.html', ctx)

def profesores(request):
    ctx = {"profesores": Profesor.objects.all()}
    return render(request, 'appDiego/profesores.html',ctx)

def alumnos(request):
    ctx = {"alumnos": Alumno.objects.all()}
    return render(request, 'appDiego/alumnos.html',ctx)

def claseForm(request):
    if request.method == "POST":
        clase = Clase(nombre=request.post['nombre'], horario=request.post['horario'])
        clase.save()
        return HttpResponse("Se grabo con exito la clase")
    
    return render (request, "appDiego/claseForm.html")

