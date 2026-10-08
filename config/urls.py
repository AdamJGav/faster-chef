from django.urls import path
from django.contrib import admin

from core.views import home
from core.views import recipes
from core.views import recipe




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("recipes/", recipes, name="recipes"),
    path("recipe/<int:recipe_id>/", recipe, name="recipe"),
]
