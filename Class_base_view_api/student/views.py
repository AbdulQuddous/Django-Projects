from rest_framework.views import APIView
from .serializer import Studentserilizer
from .models import Student_data
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Studentapi(APIView):
    def get(self , request , pk=None):
        if pk:
            try:
                student = Student_data.objects.get(id=pk)
                serializer = Studentserilizer(student)
                return Response(serializer.data)
            except:
                return Response({"message":"student not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            student=student = Student_data.objects.all()
            serializer = Studentserilizer(student,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK) 
        
    def post(self,request):
        serializer = Studentserilizer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data inserted"},status=status.HTTP_201_CREATED)
        return Response({"message":"Error"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request ,pk=None):
        try:
            student = Student_data.objects.get(id=pk)
        except:
            return Response({"message":"student not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = Studentserilizer(student ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data inserted"},status=status.HTTP_201_CREATED)
        return Response({"message":"Error"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self , request ,pk=None):
        try:
            student = Student_data.objects.get(id=pk)
        except:
            return Response({"message":"student not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = Studentserilizer(student ,data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data inserted"},status=status.HTTP_201_CREATED)
        return Response({"message":"Error"},status=status.HTTP_400_BAD_REQUEST)
    

    
    def delete(self , request , pk=None):
        try:
            student = Student_data.objects.get(id=pk)
            student.delete()
            return Response({"message":"student deleted"},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"message":"student not found"},status=status.HTTP_404_NOT_FOUND)
    


        