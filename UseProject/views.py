from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse('a')


def contato(request):
    pass
