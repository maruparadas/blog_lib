from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)

class EditorialFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    web = forms.CharField(max_length=40)
    pais_origen = forms.CharField(max_length=40)

class LibrosFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={"rows": 12}))
    creador=  forms.CharField(max_length=100)
    fecha_publicacion = forms.DateField()
    portada= forms.ImageField()

class ChatForm (forms.Form):
    chat = forms.CharField(max_length=400)