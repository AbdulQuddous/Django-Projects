from django.shortcuts import render
from .serializer import Studentserializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = Studentserializer(students , many=True)
    return Response(serializer.data)
