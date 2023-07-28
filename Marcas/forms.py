from django import forms

class BuscarForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
