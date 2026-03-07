from django.urls import path
from . import views

urlpatterns = [
    path("",views.create_session,name='create_session')
]
