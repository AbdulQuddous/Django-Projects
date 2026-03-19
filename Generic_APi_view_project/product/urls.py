from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductGetCreate.as_view(), name="ProductGetCreate"),
    path("ProductRetrieveUpdateDestroy/<int:pk>/", views.ProductRetrieveUpdateDestroy.as_view(), name="ProductRetrieveUpdateDestroy"),
]