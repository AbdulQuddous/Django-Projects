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

@api_view(['PUT', 'PATCH'])
def student_update(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializier = Studentserializer(student , data=request.data , partial= True)
    else:
        serializier = Studentserializer(student , data=request.data )

    if serializier.is_valid():
        serializier.save()
        return Response(serializier.data , status = status.HTTP_201_CREATED)
    else:
        return Response(serializier.errors, status = status.HTTP_400_BAD_REQUEST)
    