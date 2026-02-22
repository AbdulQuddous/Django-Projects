from django import forms
from .models import Student

class student_entryfrom(forms.ModelForm):
    class Meta:
        model= Student
        fields= ['user_name','firstname','lastname','email']