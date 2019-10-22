from django.contrib import admin
from django.urls import path

from .views import home_page

urlpatterns = [
    path('draggle-admin-dash/', admin.site.urls),
    path('', home_page)
]
