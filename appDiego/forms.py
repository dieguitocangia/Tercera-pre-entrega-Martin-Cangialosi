from django import forms

class ClaseFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la Clase", max_length=50, required=True)
    horario = forms.TimeField(label="Horario de la Clase", required=True)