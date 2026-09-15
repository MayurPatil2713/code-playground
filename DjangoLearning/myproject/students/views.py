from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def about(request):
    context = {
    "name":"Mayur",
    "course":"MCA",
    "is_student" : True,
}
    return render(request, "students/about.html", context)

