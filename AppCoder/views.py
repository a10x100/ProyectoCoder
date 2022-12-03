from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(request):
    curso=Curso(nombre="Python",camada="1000")
    curso.save()
    documento=f"Curso: {curso.nombre}   Camada: {curso.camada}"
    return HttpResponse(documento)
