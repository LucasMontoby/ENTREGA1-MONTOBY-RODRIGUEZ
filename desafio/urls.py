from django.urls import path
from .views import una_vista, crear, listado

urlpatterns = [
    path('', una_vista, name='base'), 
    path('blog/', listado, name='listado'),
    path('crear/', crear, name='crear'),
]