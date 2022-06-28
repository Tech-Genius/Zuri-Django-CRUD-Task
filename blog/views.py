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
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass  

class  PostDetailView(generic.DetailView):  
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')      
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')    
class PostDeleteView(generic.DeleteView):
    model = Post
    entries = Post.objects.all()
    entries.delete()
    success_url = reverse_lazy('blog:all')
