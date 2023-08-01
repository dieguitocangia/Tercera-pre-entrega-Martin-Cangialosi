from django.contrib import admin
from .models import Clase, Profesor, Alumno

# Register your models here.

admin.site.register(Clase)
admin.site.register(Profesor)
admin.site.register(Alumno)