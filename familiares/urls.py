from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.ListadoGatos.as_view(), name='listado1'),
    path('crear1/', views.CrearGato.as_view(), name='crear1'),
    path('editar1/<int:pk>/', views.EditarGato.as_view(), name='editar1'),
    path('eliminar1/<int:pk>/', views.EliminarGato.as_view(), name='eliminar1'),
    # path('mostrar1/<int:pk>/', views.MostrarGato.as_view(), name='mostrar1'),
]