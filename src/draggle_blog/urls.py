from django.contrib import admin
from django.urls import path, include

from .views import home_page, about_page, contact_page
from blog import urls

urlpatterns = [
    path("draggle-admin-dash/", admin.site.urls),
    path("", home_page),
    path("about/", about_page),
    path("contact/", contact_page),
    path("blog/", include(urls)),
]
