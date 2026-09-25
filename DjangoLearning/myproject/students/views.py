from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student

def home(request):
    return HttpResponse("Hello, Django!")


def about(request):
    students = ["Amit", "Rahul", "Sneha"]
    context = {
        "students":students
    }
    return render(request, "students/about.html", context)

def student_detail(request, student_id, name):
    return HttpResponse(f"Student ID: {student_id} Name: {name}")

def student_list(request):
    students = Student.objects.all()
    
    context = {
        "students": students
    }

    return render(request, "students/student_list.html", context)