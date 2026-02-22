from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('entry_form/',views.entry_form,name='entry_form'),
    path('student_saved/', views.student_saved, name='student_saved'),
    path('student_list/', views.student_list, name='student_list'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
]
