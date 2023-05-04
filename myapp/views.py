from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request, username: str) -> HttpResponse:
    return HttpResponse(f"<h1> Hola Buenas {username} </h1>")

def index(request) -> HttpResponse:
    return HttpResponse("<h1> Tremendo Indice Maquina </h1>")
