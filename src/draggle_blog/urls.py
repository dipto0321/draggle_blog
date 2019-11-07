from django.contrib import admin
from django.urls import path

from .views import home_page, about_page, contact_page
from blog.views import get_blog_post

urlpatterns = [
    path("draggle-admin-dash/", admin.site.urls),
    path("", home_page),
    path("about/", about_page),
    path("contact/", contact_page),
    path("blog/posts/<str:slug>/", get_blog_post),
]
