from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from . serializers import user_serializers
from rest_framework import status
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def user_list(request):
    users = User.objects.all()
    serializer = user_serializers(users , many=True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_create(request):
    serializer = user_serializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



