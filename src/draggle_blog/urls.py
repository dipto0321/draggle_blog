from django.contrib import admin
from django.urls import path, re_path

from .views import home_page, hello_world

urlpatterns = [
    path('draggle-admin-dash/', admin.site.urls),
    path('', home_page),
    re_path(r'^hello?/$', hello_world)
]
