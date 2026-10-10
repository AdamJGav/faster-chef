from django.urls import path
from django.contrib import admin

from core.views import home
from core.views import recipes
from core.views import recipe
from core.views import recipe_form




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("recipes/", recipes, name="recipes"),
    path("recipe/<int:recipe_id>/", recipe, name="recipe"),
    path("recipe_form/", recipe_form, name="recipe_create"),
    path("recipe_form/<int:recipe_id>/", recipe_form, name="recipe_edit"),
]
