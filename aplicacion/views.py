from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .form import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

def index(request):
    return render(request, "aplicacion/base.html")

def compras(request):
    return render(request, "aplicacion/compras.html")

def ventas(request):
    return render(request, "aplicacion/ventas.html")

def alquileres(request):
    ctx = {"alquileres": Alquiler.objects.all()} 
    return render(request, "aplicacion/alquileres.html", ctx)

def alquilerForm(request):
    if request.method == "POST":
        alquiler = Alquiler(nombre=request.POST['nombre'], tipo=request.POST['tipo'], precio=request.POST['precio'])
        alquiler.save()
        return HttpResponse ("Se grabo con exito el Alquiler!")
    return render(request, "aplicacion/alquilerForm.html")

def alquilerForm2(request):
    if request.method == "POST":
        miForm=AlquilerForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            alquiler=Alquiler(nombre=informacion['nombre'], tipo=informacion['tipo'], precio=informacion['precio'])
            alquiler.save()
            return render(request, "aplicacion/base.html")
    else:
       
        miForm = AlquilerForm()
    
    return render(request, "aplicacion/alquilerForm2.html", {"form": miForm})


def equipos(request):
    ctx = {"equipos": Equipo.objects.all()} 
    return render(request, "aplicacion/equipos.html", ctx)

def equipoForm(request):
    if request.method == "POST":
        equipo = Equipo(nombre=request.POST['nombre'], tipo=request.POST['tipo'])
        equipo.save()
        return HttpResponse ("Se grabo con exito el Equipo!")
    return render(request, "aplicacion/equipoForm.html")

def equipoForm2(request):
    if request.method == "POST":
        miForm=EquipoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            equipo=Equipo(nombre=informacion['nombre'], tipo=informacion['tipo'])
            equipo.save()
            return render(request, "aplicacion/base.html")
    else:
       
        miForm = EquipoForm()
    
    return render(request, "aplicacion/equipoForm2.html", {"form": miForm})


def buscarPrecio(request):
    return render(request, "aplicacion/buscarPrecio.html")

def buscar2(request):
    if request.GET['precio']:
        precio=request.GET['precio']
        alquileres=Alquiler.objects.filter(precio__icontains=precio)
        return render(request, 
                       "aplicacion/resultadosPrecio.html",
                      {"precio":precio, "alquileres":alquileres})
    return HttpResponse("No se ingresaron datos!")
    
#___________ update delete create (Alquileres)_______

def alquileres(request):
    ctx = {"alquileres": Alquiler.objects.all()} 
    return render(request, "aplicacion/alquileres.html", ctx)

def updateAlquiler(request, id_alquiler):
    alquiler = Alquiler.objects.get(id=id_alquiler)
    if request.method == "POST":
        miForm = AlquilerForm(request.POST)
        if miForm.is_valid():
            alquiler.nombre = miForm.cleaned_data.get('nombre')
            alquiler.tipo = miForm.cleaned_data.get('tipo')
            alquiler.precio = miForm.cleaned_data.get('precio')
            alquiler.save()
            return redirect(reverse_lazy('alquileres'))
    else:
        miForm = AlquilerForm(initial={'nombre':alquiler.nombre,
                                       'tipo':alquiler.tipo,
                                       'precio':alquiler.precio})
    
    return render(request, "aplicacion/alquilerForm.html", {'form': miForm})  
   
def deleteAlquiler(request, id_alquiler):
    alquiler = Alquiler.objects.get(id=id_alquiler)
    alquiler.delete()
    return redirect(reverse_lazy('alquileres'))

def createAlquiler(request):
    if request.method == "POST":
        miForm=AlquilerForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_tipo = miForm.cleaned_data.get('tipo')
            p_precio = miForm.cleaned_data.get('precio')
            alquiler=Alquiler(nombre=p_nombre, tipo=p_tipo, precio=p_precio)
            alquiler.save()
            return redirect(reverse_lazy('alquileres'))
    else:   
        miForm = AlquilerForm()
    
    return render(request, "aplicacion/alquilerForm.html", {"form": miForm})

#____class views Equipo_____

class EquipoList(ListView):
    model = Equipo

class EquipoCreate(CreateView):
    model = Equipo
    fields = ['nombre','tipo']
    success_url = reverse_lazy('equipos')

class EquipoDetail(DetailView):
    model = Equipo