from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .forms import BusquedaBlog, FormBlog
from .models import Blog
from datetime import datetime

# Create your views here.

def una_vista(request):
    return render(request, 'index.html')

def crear(request):
    if request.method == 'POST':
        form = FormBlog(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            blog = Blog(
                nombre=data.get('nombre'),
                edad=data.get('edad'),
                fecha_creacion=fecha
            )
            blog.save()

            
            return redirect('listado')
        
        else:
            return render(request, 'crear.html', {'form': form})
            
    
    form_blog = FormBlog()
    
    return render(request, 'crear.html', {'form': form_blog})

def listado(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listado = Blog.objects.filter(nombre__icontains=nombre_de_busqueda) 
    else:
        listado = Blog.objects.all()
    
    form = BusquedaBlog()
    return render(request, 'listado.html', {'listado': listado, 'form': form})