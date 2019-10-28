from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse("<h1>Home Page View</h1>")


def hello_world(request):
    return render(request, "hello_world.html")
