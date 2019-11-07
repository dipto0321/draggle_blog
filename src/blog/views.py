from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def get_blog_post(request, slug):
    blog_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post.html"
    context = {"blog_obj": blog_obj, "title": "Blog Posts Detail"}
    return render(request, template_name, context)


def blog_post_list_view(request):
    template_name = "blog_posts/index.html"
    context = {"post_list": [], "title": "Post List"}
    return render(request, template_name, context)


def blog_post_create_view(request):
    pass


def blog_post_retrive_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_posts/retrive.html"
    context = {"post": post_obj}
    return render(request, template_name, context)


def blog_post_update_view(request):
    pass


def blog_post_delete_view(request):
    pass

