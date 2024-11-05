from django.shortcuts import render,redirect
from .models import Materia
# Create your views here.

def inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"mismaterias" :lasmaterias})

def registrarMaterias(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtmateria"]
    creditos=request.POST["numcreditos"]

    guardarmaterias=Materia.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)

    return redirect('/')
    
