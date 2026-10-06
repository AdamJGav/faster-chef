from django.urls import path

from core.views import home
from core.views import recipes



urlpatterns = [
    path("", home, name="home"),
    path("recipes/", recipes, name="recipes"),
]
