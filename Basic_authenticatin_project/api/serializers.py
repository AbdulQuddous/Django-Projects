from django.contrib.auth.models import User
from rest_framework import serializers
class user_serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email']