from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post(request):
    if request.method=='GET':
        return Response({"message":"Public view everyone access"})
    elif request.method=='POST':
        return Response({"message":f"Request bus user {request.user.username}"})