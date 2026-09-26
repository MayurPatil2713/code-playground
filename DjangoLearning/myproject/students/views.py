from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from students.models import Student
from students.forms import StudentForm
from students.forms import StudentModelForm

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

def student_form(request):

    if request.method == "POST":
        sf = StudentForm(request.POST)

        if sf.is_valid():
            print("Form is valid")
            print(sf.cleaned_data)
        else:
            print("Form is invalid")
            print(sf.errors)
    else:
        sf = StudentForm()
    context = {
        "form": sf
    }
    return render(request, "students/student_form.html", context)

def student_create(request):

    if request.method == "POST":
        form = StudentModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student created successfully")
            return redirect("student_list")
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        form = StudentModelForm()
    context = {
        "form":form 
    }
    return render(request, "students/student_form.html", context)

def student_edit(request, student_id):

    student = Student.objects.get(id=student_id)
    
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect("student_list")
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        form = StudentModelForm(instance=student)
    context = {
        "form":form 
    }
    return render(request, "students/student_form.html", context)

def student_delete(request, student_id):

    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect("student_list")
    else:
        context = {
            "student":student
        }
        return render(request, "students/student_confirm_delete.html", context)

            