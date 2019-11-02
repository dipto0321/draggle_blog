from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def get_blog_post(request):
    blog_obj = BlogPost.objects.get(id=1)
    template_name = "blog_post_detail.html"
    context = {"blog_obj": blog_obj, "title": "Blog Posts Detail"}
    return render(request, template_name, context)

