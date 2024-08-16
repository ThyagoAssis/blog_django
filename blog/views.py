from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ["titulo", "conteudo", "foto"]
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["titulo", "conteudo", "foto"]
    success_url = reverse_lazy('blog_list')
    

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')