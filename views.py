from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola Mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

