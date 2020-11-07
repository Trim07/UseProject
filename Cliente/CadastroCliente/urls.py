from django.urls import path, include
from .views import index, cadastrarCliente, cadastrarGrupoCliente

urlpatterns = [
    path('', index, name='index'),
    path('cadastrarcliente/', cadastrarCliente, name='cadastrarCliente'),
    path('cadastrargrupocliente/', cadastrarGrupoCliente, name='cadastrarGrupoCliente')
]