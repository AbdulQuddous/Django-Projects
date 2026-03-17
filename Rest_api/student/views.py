from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Student_data
from .serializer import Student_serializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def student_list(request):
    students = Student_data.objects.all()
    serializer = Student_serializer(students , many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    serializer = Student_serializer(data =request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_student(request , pk):
    try:
        student = Student_data.objects.get(id=pk)
    except:
        return Response({"error": "Student not found"}, status=404)
       
    if request.method == "PATCH":
        serializer = Student_serializer(student , data = request.data , partial=True)
    else:
        serializer = Student_serializer(student , data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request , pk):
    try:
        student = Student_data.objects.get(id=pk)
    except:
        return Response({"error": "Student not found"}, status=404)
    
    student.delete()
    return Response({"message":"Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
        