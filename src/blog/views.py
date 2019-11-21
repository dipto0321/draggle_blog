from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import BlogPostModelForm
from helpers.utils import slug_generator


def blog_post_list_view(request):
    post_list = BlogPost.objects.all()
    template_name = "blog_posts/index.html"
    context = {"post_list": post_list, "title": "Post List"}
    return render(request, template_name, context)


def blog_post_create_view(request):
    post_form = BlogPostModelForm(request.POST or None)
    if post_form.is_valid():
        post_obj = post_form.save(commit=False)
        post_obj.slug = slug_generator(post_obj.title)
        post_obj.save()
        post_form = BlogPostModelForm()
    template_name = "blog_posts/create.html"
    context = {"post_form": post_form, "title": "Post Create"}
    return render(request, template_name, context)


def blog_post_retrive_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_posts/retrive.html"
    context = {"post": post_obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_posts/update.html"
    context = {"form": None, "post_obj": post_obj}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_posts/delete.html"
    context = {"post_obj": post_obj}
    return render(request, template_name, context)

