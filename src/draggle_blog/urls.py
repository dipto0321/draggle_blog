from django.contrib import admin
from django.urls import path

from .views import home_page, about_page, contact_page
from blog.views import blog_post_list_view, blog_post_retrive_view

urlpatterns = [
    path("draggle-admin-dash/", admin.site.urls),
    path("", home_page),
    path("about/", about_page),
    path("contact/", contact_page),
    path("blog/", blog_post_list_view),
    path("blog/<str:slug>/", blog_post_retrive_view),
]
