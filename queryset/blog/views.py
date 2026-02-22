from django.shortcuts import render
from . models import Student
from django.db.models import Q
# Create your views here.
def student_view(request):
    search = request.GET.get('search')
    city = request.GET.get('city')

    students = Student.objects.all()

    if search:
        students = students.filter(
            Q(name__icontains=search) 
        )

    if city:
        students = students.filter(city=city)

    return render(request, 'blog/s.html', {'students': students})

