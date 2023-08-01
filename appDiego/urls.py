from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name='inicio' ),
    path('profesores',profesores, name='profesores' ),
    path('clases',clases, name='clases' ),
    path('alumnos',alumnos, name='alumnos' ),

    path('clase_form/', claseForm, name="clase_form" ),
]