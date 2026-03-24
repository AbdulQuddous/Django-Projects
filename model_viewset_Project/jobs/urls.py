from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("jobs",views.Job_view_set,basename='jobs')

urlpatterns = [
    path('',include(router.urls))
]
