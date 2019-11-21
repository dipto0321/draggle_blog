from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    template_name = "static/home.html"
    context = {"title": "Home", "content": "Awesome Draggle Blog app!"}
    return render(request, template_name, context)


def about_page(request):
    template_name = "static/about.html"
    context = {"title": "About"}
    return render(request, template_name, context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    template_name = "static/contact.html"
    context = {"title": "Contact", "form": form}
    return render(request, template_name, context)
