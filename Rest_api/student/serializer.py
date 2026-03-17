from rest_framework import serializers
from . import models

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student_data
        fields = "__all__"