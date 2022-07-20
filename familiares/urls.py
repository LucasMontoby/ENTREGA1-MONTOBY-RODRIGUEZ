from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.Listado1.as_view(), name='listado1'),
    path('crear1/', views.Crear1.as_view(), name='crear1'),
    path('editar1/<int:pk>/', views.Editar1.as_view(), name='editar1'),
    path('eliminar1/<int:pk>/', views.Eliminar1.as_view(), name='eliminar1'),
    # path('mostrar1/<int:pk>/', views.MostrarGato.as_view(), name='mostrar1'),
]

