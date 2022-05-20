import requests
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts_search'
    ordering = ['-time_add_post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreate(CreateView):
    template_name = 'news_create.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_types = 'ne'
        return super().form_valid(form)


class ArticleCreate(CreateView):
    template_name = 'news_create.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_types = 'ar'
        return super().form_valid(form)


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    ordering = ['-time_add_post']
    paginate_by = 10


class PostDetail(DetailView):
    model = Post  #
    template_name = 'news_text.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'