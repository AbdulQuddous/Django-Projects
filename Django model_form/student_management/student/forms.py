from django.forms import ModelForm
from .models import Student_data

class student_entry_form(ModelForm):
    class Meta:
        model = Student_data
        fields = '__all__'
