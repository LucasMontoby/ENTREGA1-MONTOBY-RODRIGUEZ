from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Personal


class ListadoPersonal(ListView):
    model=Personal
    template_name = 'Personal/listado1.html'
    
class CrearPersonal(CreateView):
    model=Personal
    template_name = 'Personal/crear1.html'
    success_url = '/familiares/Personal'
    fields = ['apellido', 'edad', 'fecha_creacion']


class EditarPersonal(LoginRequiredMixin, UpdateView):
    model=Personal
    template_name = 'Personal/editar1.html'
    success_url = '/familiares/Personal'
    fields = ['apellido', 'edad', 'fecha_creacion']


class EliminarPersonal(LoginRequiredMixin, DeleteView):
    model=Personal
    template_name = 'Personal/eliminar1.html'
    success_url = '/familiares/Personal'


class MostrarPersonal(DetailView):
    model = Personal