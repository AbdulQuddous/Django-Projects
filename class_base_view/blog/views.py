from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy


class list_View(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class detail_view(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class create_view(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title' , 'content']

class update_view(UpdateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title' , 'content']

class delete_view(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('list_view')







