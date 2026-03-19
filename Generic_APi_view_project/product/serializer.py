from . import models
from rest_framework import serializers

class PRODUCTSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = "__all__"