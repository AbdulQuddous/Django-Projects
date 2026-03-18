from .models import Student_data
from rest_framework import serializers

class Studentserilizer(serializers.ModelSerializer):
    class Meta:
        model = Student_data
        fields= "__all__"