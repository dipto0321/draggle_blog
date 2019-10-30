from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse("<h1>Home Page View</h1>")


def hello_world(request):
    focus_message = "Hey! This is Django"
    title = "Hello! Django"
    return render(
        request, "hello_world.html", {"title": title, "focus_message": focus_message}
    )
