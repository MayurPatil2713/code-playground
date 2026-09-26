from django import forms
from students.models import Student

class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    course = forms.CharField()

class StudentModelForm(forms.ModelForm):

    class Meta:
        model = Student 
        fields = ["name", "age", "email", "course"]