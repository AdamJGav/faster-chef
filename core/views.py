from django.shortcuts import render


def home(request):
    return render(request, "home.jinja", using="jinja2")

def recipes(request):
    recipes = [1,2]

    return render(request, "recipes.jinja", using="jinja2", context={
        "recipes": recipes
    })
