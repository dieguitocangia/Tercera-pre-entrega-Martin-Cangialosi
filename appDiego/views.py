from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


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
        nuevoForm=ClaseFormulario(request.POST)
        print(nuevoForm)
        if nuevoForm.is_valid:
            informacion = nuevoForm.cleaned_data
            clase = Clase(nombre=informacion['nombre'], horario=informacion['horario'])
            clase.save()
            return render(request, 'appDiego/base.html')
    else:
        nuevoForm = ClaseFormulario()

    return render(request, 'appDiego/claseForm.html', {"form":nuevoForm})

def buscarClase(request):
    return render(request,'appDiego/buscarClase.html')

def buscar2(request):
    if request.GET['clase']:
        clase=request.GET['clase']
        horarios= Clase.objects.filter(nombre__icontains=clase)
        return render(request, "appDiego/resultadosClase.html",{"clases": clase, "horarios": horarios })
    return HttpResponse("No se ingresaron datos para buscar")
