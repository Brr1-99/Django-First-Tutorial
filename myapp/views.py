from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Subject

# Create your views here.
def hello(request, username: str) -> HttpResponse:
    return HttpResponse(f"<h1> Hola Buenas {username} </h1>")

def index(request) -> HttpResponse:
    return render(request, template_name='index.html')

def subject(request) -> JsonResponse:
    subjects = list(Subject.objects.values())
    return JsonResponse(subjects, safe=False)

def subject_or_404(request, name: str) -> JsonResponse:
    subjects = get_object_or_404(Subject, name=name)
    return HttpResponse(subjects.description)