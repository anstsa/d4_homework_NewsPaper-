from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import render
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm




class NewsList (ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

      

class NewDetail (DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    queryset = Post.objects.all()


class Search (ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    queryset = Post.objects.order_by('-id')
    #ordering = ['-price']
   
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) 
        return context 
    
 
class PostAdd (CreateView):
    template_name = 'new_add.html'
    form_class = PostForm

class PostEdit(UpdateView):
    template_name = 'new_add.html'
    form_class = PostForm
 
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
 
 
class PostDelete(DeleteView):
    template_name = 'new_delete.html'
    queryset = Post.objects.all()
    context_object_name = 'new'
    success_url = '/news/'


