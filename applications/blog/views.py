from django.views.generic import ListView, DetailView
from django.db.models import Count
from . models import Blog, Post, Tags, Category
# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog.html"
    ordering = 'id'
    paginate_by = 6
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular'] = Post.objects.get_popular_posts()
        context['tags'] = Tags.objects.all()
        context['categorycount'] = Category.objects.catidad_por_categoria()
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blogDetail.html"
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view += 1
        obj.save()
        return obj
