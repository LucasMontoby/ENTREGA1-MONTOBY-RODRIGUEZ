from django.urls import path
from .views import crear, una_vista, un_template

urlpatterns = [
    path('', una_vista),
    path('un-template', un_template),
    path('crear', crear),
    #path('blog/', listado, name='listado'),
    #path('crear/', crear, name='crear'),
]

