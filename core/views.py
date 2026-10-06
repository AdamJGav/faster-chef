from django.shortcuts import render


def home(request):
    return render(request, "home.jinja", using="jinja2")
