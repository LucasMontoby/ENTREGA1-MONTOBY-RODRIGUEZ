from django.http import HttpResponse
from django.shortcuts import render
from desafio.models import Familiar as flia
from django.template import loader


# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Proyecto</h1>')



def un_template(request):
    
    familiares = flia.objects.all() #Traer la información 
    
    dicc = { "familiares" : familiares} #relacionar la info de un dicc con un html
    
    plantilla = loader.get_template('index.html') #Cargar la plantilla del html

    documento = plantilla.render(dicc) #renderizar la información
    
    return HttpResponse(documento) #retornamos la renderización


def crear(request):
    
    familiar1 = flia(nombre="Lucas", phone= 123456, fecha_nacimiento= '1983-5-14')
    familiar2 = flia(nombre="Lucas", phone= 123456, fecha_nacimiento= '1983-5-14')
    familiar3 = flia(nombre="Lucas", phone= 123456, fecha_nacimiento= '1983-5-14')
    
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    return HttpResponse('Se cargo con exito')