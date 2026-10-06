from django.shortcuts import render


def home(request):
    return render(request, "home.jinja", using="jinja2")

def meals(request):
    return render(request, "meals.jinja", using="jinja2")
