from django.urls import path
from . import views 

urlpatterns = [
    path("student_Create/",views.student_create,name="student_create"),
    path('',views.student_list,name='student_list'),
    path('student_data/<int:pk>/',views.student_data,name='student_data'),
    path('student_delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('student_update/<int:pk>/', views.student_update, name='student_update'),
]
