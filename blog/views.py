from django.shortcuts import render
from .models import Post
from django.urls import reverse,reverse_lazy

from django.views import generic

class  PostListView(generic.ListView):
    model = Post

class  PostCreateView(generic.CreateView):  
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')  

class  PostDetailView(generic.DetailView):  
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')      
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')    
class PostDeleteView(generic.DeleteView):
    entries = Post.objects.all()
    entries.delete()
