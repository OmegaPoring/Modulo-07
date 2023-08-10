from django.shortcuts import render, HttpResponseRedirect
from .models import Laboratorio

# Create your views here.

def index(request):
     return render(request, "laboratorio/index.html")

def labs(request):
    laboratorios = Laboratorio.objects.all()
    context = {
    'laboratorios': laboratorios,
    }

    return render(request, "laboratorio/laboratorios.html", context)

def agregar(request):
    if request.method == "POST":
        Laboratorio.objects.create(
            name=request.POST["name"],
            city=request.POST["city"],
            country=request.POST["country"],
        )
        return HttpResponseRedirect("/laboratorios/")
    elif request.method == "GET":
        return render(request, "laboratorio/agregar.html")
    
def eliminar(request, id):
        laboratorio=Laboratorio.objects.get(id=id)
        laboratorio.delete()
        return HttpResponseRedirect("/laboratorios/")

def confirmar(request, id):
     laboratorio=Laboratorio.objects.get(id=id)
     context = {"laboratorio": laboratorio}
     return render(request, "laboratorio/eliminar.html", context)
    
def actualizar(request, id):
    laboratorio = Laboratorio.objects.filter(id=id)
    if request.method == "POST":
        laboratorio.update(
            name=request.POST["name"],
            city=request.POST["city"],
            country=request.POST["country"],
        )
        return HttpResponseRedirect("/laboratorios/")
    elif request.method == "GET":
        laboratorio = Laboratorio.objects.get(id=id)
        context = {"laboratorio": laboratorio}
        return render(request, "laboratorio/actualizar.html", context)