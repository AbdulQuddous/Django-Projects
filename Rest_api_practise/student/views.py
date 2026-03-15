from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def student_list(request):
    students= Student.objects.all()
    serializer= Studentserializer(students , many=True)
    return Response(serializer.data)

@api_view(['POST'])
def student_add(request):
    serializer = Studentserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)