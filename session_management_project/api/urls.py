from .views import user_list,user_create
from django.urls import path

urlpatterns = [
    path('',user_list,name='user_list'),
     path('user_create/',user_create,name='user_create')
]
