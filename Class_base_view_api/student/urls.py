from django.urls import path
from . import views

urlpatterns = [
    path("Studentapi",views.Studentapi.as_view(),name='Studentapi'),
    path("Studentapi/<int:pk>/",views.Studentapi.as_view(),name='Studentapi'),
]
