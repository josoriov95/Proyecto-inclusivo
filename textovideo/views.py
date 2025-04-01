from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hola inmundo animal</h1>")
def root(request):
    return HttpResponse("<h1>Inicio sesion</h1>")