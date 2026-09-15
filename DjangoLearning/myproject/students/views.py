from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def about(request):
    return HttpResponse("This is my first Django project.")



