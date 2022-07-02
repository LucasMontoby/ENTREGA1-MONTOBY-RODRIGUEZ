from django.http import HttpResponse
from django.shortcuts import render
from desafio.models import Blog
from django.template import loader


# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Proyecto</h1>')

def un_template(request):
    
    familiares = Blog.objects.all() #Traer la información 
    
    dicc = { "familiares" : familiares} #relacionar la info de un dicc con un html
    
    plantilla = loader.get_template('index.html') #Cargar la plantilla del html

    documento = plantilla.render(dicc) #renderizar la información
    
    return HttpResponse(documento) #retornamos la renderización


def crear(request):
    
    familiar1 = Blog(nombre="Lucas", edad= 12, fecha_creacion= '2022-5-14')
    familiar2 = Blog(nombre="Lucas", edad= 13, fecha_creacion= '2021-5-14')
    familiar3 = Blog(nombre="Lucas", edad= 14, fecha_creacion= '2020-5-14')
    
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    return HttpResponse('Se cargo con exito')