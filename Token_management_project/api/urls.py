from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('auth-token/',obtain_auth_token,name='api_auth_token'),
    path('profile/',views.user_profile, name='user_profile'),
    path('admin-panel',views.admin_panel,name='admin_panel')
]
