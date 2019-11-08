from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_post_list_view(request):
    post_list = BlogPost.objects.all()
    template_name = "index.html"
    context = {"post_list": post_list, "title": "Post List"}
    return render(request, template_name, context)


def blog_post_create_view(request):
    template_name = "create.html"
    context = {"form": None, "title": "Post Create"}
    return render(request, template_name, context)


def blog_post_retrive_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "retrive.html"
    context = {"post": post_obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "update.html"
    context = {"form": None, "post_obj": post_obj}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "delete.html"
    context = {"post_obj": post_obj}
    return render(request, template_name, context)

