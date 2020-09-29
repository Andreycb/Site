from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        list_post = Post.objects.all()
        paginator = Paginator(list_post, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_posts = paginator.page(page)
        except PageNotAnInteger:
            file_posts = paginator.page(1)
        except EmptyPage:
            file_posts = paginator.page(paginator.num_pages)
            
        context['list_posts'] = file_posts
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
