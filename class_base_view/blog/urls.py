from django.urls import path
from .views import list_View, detail_view, create_view, update_view, delete_view

urlpatterns = [
    # List all posts
    path('', list_View.as_view(), name='list_view'),

    # Detail view for a single post (by primary key)
    path('detail/<int:pk>/', detail_view.as_view(), name='post_detail'),

    # Create a new post
    path('create/', create_view.as_view(), name='post_create'),

    # Update an existing post
    path('update/<int:pk>/', update_view.as_view(), name='post_update'),

    # Delete a post
    path('delete/<int:pk>/', delete_view.as_view(), name='post_delete'),
]