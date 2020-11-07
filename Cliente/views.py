from django.db.transaction import atomic, DatabaseError, savepoint, savepoint_commit, savepoint_rollback
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect


def index(request):
    return HttpResponse('Pagina index de Cliente')

