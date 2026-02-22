from django.shortcuts import render,redirect,get_object_or_404
from .forms import student_entry_form
from .models import Student_data
# Create your views here.
def home(request):
    return render(request, 'student/home.html')

def entry_form(request):
    if request.method=='POST':
        form=student_entry_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_saved')
    else:
        form = student_entry_form()              
    return render(request, 'student/entry_form.html', {'form': form})

    
def student_saved(request):
    return render(request, 'student/student_saved.html')

def student_list(request):
    students = Student_data.objects.all()
    return render(request,'student/student_list.html',{'students':students})

def delete_student(request,pk):
    student_d=get_object_or_404(Student_data,pk=pk)
    if request.method=='POST':
        student_d.delete()
        return redirect('student_list')
    return render(request, 'student/delete_confirmation.html', {'student': student_d})