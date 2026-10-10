from django.shortcuts import get_object_or_404, redirect, render

from core.forms import RecipeForm
from core.models import Recipe


def home(request):
    return render(request, "home.jinja", using="jinja2")

def recipes(request):
    recipes = Recipe.objects.all()
    return render(
        request,
        "recipes.jinja",
        using="jinja2",
        context={"recipes": recipes},
    )

def recipe(request, recipe_id):
    recipe = get_object_or_404(
        Recipe.objects.prefetch_related("ingredients", "steps"),
        id=recipe_id,
    )
    return render(
        request,
        "recipes/recipe.jinja",
        using="jinja2",
        context={"recipe": recipe},
    )

def recipe_form(request, recipe_id=None):

    # get existing recipe for edit
    recipe = (
        get_object_or_404(Recipe, id=recipe_id)
        if recipe_id is not None
        else None
    )

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            saved_recipe = form.save()
            return redirect("recipe", recipe_id=saved_recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(
        request,
        "recipes/recipe_form.jinja",
        using="jinja2",
        context={"form": form, "recipe": recipe}
    )