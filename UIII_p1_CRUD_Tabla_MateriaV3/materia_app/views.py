from django.shortcuts import render,redirect
from .models import Materia
# Create your views here.

def inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"mismaterias" :lasmaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtmateria"]
    creditos=request.POST["numcreditos"]

    guardarmaterias=Materia.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)

    return redirect('/')
    

def seleccionarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})

def editarMateria(request,codigo):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtmateria"]
    creditos=request.POST["numcreditos"]
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save()
    redirect('/')
    

def borrarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete()
    
    return redirect('/')


