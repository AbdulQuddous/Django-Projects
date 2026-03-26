from . import views
from django.urls import path
urlpatterns = [
    path('profile/',views.post,name='profile')
]
