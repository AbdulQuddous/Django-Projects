from django.shortcuts import render
from rest_framework import viewsets
from .models import Jobs
from .serializers import Jobsserialaizers
# Create your views here.
class Job_view_set(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = Jobsserialaizers
