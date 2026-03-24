from rest_framework import serializers
from . models import Jobs

class Jobsserialaizers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"