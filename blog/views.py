from django.shortcuts import render
from models import Post
.
from django.views import generic

class  PostListView(generic.ListView):
    model = Post

class  PostCreateView(generic.CreatetView):  
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)  

class  PostDetailView(generic.DetailView):
    model = Post  
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)      