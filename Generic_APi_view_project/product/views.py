from rest_framework import generics,mixins
from .models import Products
from .serializer import PRODUCTSERIALIZER

# Create your views here.
class ProductGetCreate(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Products.objects.all()
    serializer_class = PRODUCTSERIALIZER

    def get(self , request , *args , **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self , request , *args , **kwargs):
        return self.create(request, *args, **kwargs)
    
class ProductRetrieveUpdateDestroy(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Products.objects.all()
    serializer_class = PRODUCTSERIALIZER
    def get(self , request , *args , **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self , request , *args , **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    
