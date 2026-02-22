from django.shortcuts import render,redirect,get_object_or_404
from .forms import student_entryfrom
from .models import Student
# Create your views here.
def student_create(request):
    form =student_entryfrom()
    if request.method == 'POST':
        form = student_entryfrom(request.POST)
        if form.is_valid():
            form.save()
            return render(request , 'student/student_saved.html')
    return render(request , 'student/student_create.html' , {'forms':form})

def student_list(request):
    Students= Student.objects.all()
    return render(request, 'student/student_list.html',{"students":Students})

def student_data(request,pk):
    student_d=get_object_or_404(Student,pk=pk)
    return render(request,'student/student_data.html', {'student':student_d})

def student_delete(request,pk):
    Student_del=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        Student_del.delete()
        return redirect('student_list')
    return render(request, 'student/student_confirm_delete.html', {'student': Student_del})

def student_update(request,pk):
    Student_s=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        form=student_entryfrom(request.POST, instance=Student_s)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=student_entryfrom(instance=Student_s)
    return render(request,'student/student_create.html',{'forms':form})
        

