from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import libro
from .form import Libroform
from django.contrib.auth.decorators import login_required


# Create your views here.

#Acceso al sitio:
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# Acceso a las páginas
@login_required
def libros(request):
    libros = libro.objects.all() #Traemos todos los datos del objecto
    return render(request, 'libros/index.html', {'Libros':libros})

@login_required
def crear(request):
    formulario = Libroform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

@login_required
def editar(request, id):
    libro1 = libro.objects.get(id=id)
    formulario = Libroform(request.POST or None, request.FILES or None, instance=libro1)
    if formulario.is_valid and request.POST:
        formulario.save()
    return render(request, 'libros/editar.html', {'formulario': formulario})

@login_required
def borrar(request, id):
    libro1 = libro.objects.get(id=id)
    libro1.delete()
    return redirect('libros')
    #return render(request, 'libros/index.html', {"libros": libros, "mensaje": 'OK'})