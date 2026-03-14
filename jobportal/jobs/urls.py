from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView
)

urlpatterns = [

    path('', JobListView.as_view(), name='job_list'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),

    path('job/create/', JobCreateView.as_view(), name='job_create'),

    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),

    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),

    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    path('search/', views.job_search, name='job_search'),

    path('save/<int:job_id>/', views.save_jobs, name='save_job'),

    path('saved-jobs/', views.save_jobs, name='saved_jobs'),

    path('set-theme/', views.set_theme, name='set_theme'),

    path('dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),

]