from django.urls import path
from . import views

urlpatterns = [
    path('',views.upload,name='upload'),
    path('profile_view/',views.profile_view,name='profile_view')
]
