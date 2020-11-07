from django.db import DatabaseError
from django.db.transaction import atomic, savepoint, savepoint_commit, savepoint_rollback
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CadastroCliente
from .forms import CadastrarClienteForms, CadastrarGrupoClienteForms


def index(request):
    return render(request, 'lista_clientes_templates.html', context={'lista_clientes': CadastroCliente.objects.only('cnpj')})


@atomic
def cadastrarCliente(request):
    if str(request.method) == 'POST':
        savepoint_data = savepoint()
        form = CadastrarClienteForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                savepoint_commit(savepoint_data)
                return HttpResponse('Salvo com sucesso')
            except DatabaseError:
                savepoint_rollback(savepoint_data)
                return HttpResponse(DatabaseError)
        else:
            return redirect('/cadastrarcliente/')
    else:
        return render(request, 'cadastrar_cliente_templates.html', {'form': CadastrarClienteForms})


@atomic()
def cadastrarGrupoCliente(request):
    if str(request.method) == 'POST':
        savepoint_data = savepoint()
        form = CadastrarGrupoClienteForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                savepoint_commit(savepoint_data)
                return HttpResponse('Salvo com sucesso')
            except DatabaseError:
                savepoint_rollback(savepoint_data)
                return HttpResponse(DatabaseError)
        else:
            return redirect('/cadastrargrupocliente/')
    else:
        return render(request, 'cadastrargrupo_cliente_templates.html', {'form': CadastrarGrupoClienteForms})
