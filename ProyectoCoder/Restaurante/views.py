from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from Restaurante.models import Reservaciones



def inicio(request):
    return render(request, "Restaurante\inicio.html")

def menu(request):
    return render(request, "Restaurante\menu.html")

def bebidas(request):
    return render(request, "Restaurante\Bebidas.html")

def reservaciones(request):
    
    if request.method == 'POST':
        
        nombre = request.POST['nombre']
        contacto = request.POST['contacto']
        Reservaciones.objects.create(nombre=nombre, contacto=contacto)
    
        
        return redirect("reservaciones")
    
    return render(request, "Restaurante/Reservaciones.html")