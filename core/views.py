from django.shortcuts import render

from core.models import Recipe


def home(request):
    return render(request, "home.jinja", using="jinja2")

def recipes(request):
    recipes = [1,2]

    return render(request, "recipes.jinja", using="jinja2", context={
        "recipes": recipes
    })

def recipe(request, recipe_id):
    # Fetch the recipe based on the ID
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe.jinja", using="jinja2", context={
        "recipe": recipe
    });
