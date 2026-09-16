from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")


def about(request):
    students = ["Amit", "Rahul", "Sneha"]
    context = {
        "students":students
    }
    return render(request, "students/about.html", context)

