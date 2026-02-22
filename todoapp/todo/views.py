from django.shortcuts import render,redirect ,get_object_or_404
from .models import Task
from django.urls import reverse


def task_list(request):
    tasks= Task.objects.all().order_by('-created_at')
    return render(request , 'todo/task_list.html', {'tasks':tasks})


def task_create(request):
    if request.method == 'POST':
        title=request.POST.get('title', '').strip()
        description=request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
            return redirect(reverse('todo:task_list'))
        error="Title can not be empty"
        return render(request,'todo/task_form.html',{'error':error})
    return render(request,'todo/task_form.html')

def task_update(request, pk):
    task= get_object_or_404(Task, pk=pk)
    if request.method== 'post':
        title=request.POST.get('title', '').strip()
        description=request.POST.get('description')
        completed=request.post.get('completed')=='on'
        if title:
            task.title=title
            task.description=description
            task.completed=completed
            task.save()
            return redirect(reverse('todo:task_list'))
        return render(request, 'todo/task_form.html',{'task':task, 'error':'Title can not be empty.'})
    return render(request, 'todo/task_form.html',{'task':task})

def task_delete(request,pk):
    task=get_object_or_404(Task, pk=pk)
    if request.method == 'post':
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request, 'todo/task_confirm_delete.html',{'task':task})

def task_complete(request,pk):
    task=get_object_or_404(Task , pk=pk)
    if request.method=='post':
        task.completed = not task.completed
        task.save()
    return redirect('todo:task_list')