from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from helpers.utils_libs import slug_generator
from .models import BlogPost
from .forms import BlogPostModelForm


def blog_post_list_view(request):
    post_list = BlogPost.objects.all()
    template_name = "blog_posts/index.html"
    context = {"post_list": post_list, "title": "All post"}
    return render(request, template_name, context)


# @login_required
@staff_member_required
def blog_post_create_view(request):
    post_form = BlogPostModelForm(request.POST or None)
    if post_form.is_valid():
        post_obj = post_form.save(commit=False)
        post_obj.slug = slug_generator(post_obj.title)
        post_obj.user = request.user
        post_obj.save()
        post_form = BlogPostModelForm()
    template_name = "blog_posts/post_form.html"
    context = {"post_form": post_form,
               "title": "Create Post", "btn_name": "Make post"}
    return render(request, template_name, context)


def blog_post_retrive_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_posts/retrive.html"
    context = {"post": post_obj, "title": post_obj.title}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    post_form = BlogPostModelForm(request.POST or None, instance=post_obj)
    if post_form.is_valid():
        post_form.save()
        return redirect(f"/blog/{slug}")
    template_name = "blog_posts/post_form.html"
    context = {"post_form": post_form,
               "title": f"Update {post_obj.title}",
               "btn_name": "Update",
               "post_url": post_obj.get_post_retrive_url
               }
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    post_obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post_obj.delete()
        return redirect('/blog/')
    template_name = "blog_posts/delete.html"
    context = {"post": post_obj, "title": "Delete Confirmation"}
    return render(request, template_name, context)
