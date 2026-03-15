from django.urls import path
from . import views

urlpatterns = [
    path('student_list/',views.student_list,name='student_list'),
    path('student_add/',views.student_add,name='student_add'),
    path('student_update/<int:pk>/',views.student_update,name='student_update')
]
