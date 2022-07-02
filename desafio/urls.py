from django.urls import path
from .views import una_vista, crear, listado

urlpatterns = [
    path('', una_vista, name= 'index'),
    path('blog/', crear, name='crear'),
    path('blog/', listado, name='listado'),
   
]