from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    template_name = "home.html"
    context = {"title": "Home", "content": "Awesome Draggle Blog app!"}
    return render(request, template_name, context)


def about_page(request):
    template_name = "about.html"
    context = {"title": "About"}
    return render(request, template_name, context)


def contact_page(request):
    template_name = "contact.html"
    context = {"title": "Contact"}
    return render(request, template_name, context)
