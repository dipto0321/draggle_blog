from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def get_blog_post(request, post_id):
    blog_obj = get_object_or_404(BlogPost, id=post_id)
    template_name = "blog_post.html"
    context = {"blog_obj": blog_obj, "title": "Blog Posts Detail"}
    return render(request, template_name, context)

