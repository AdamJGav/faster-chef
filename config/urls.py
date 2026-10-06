from django.urls import path

from core.views import home
from core.views import meals



urlpatterns = [
    path("", home, name="home"),
    path("meals/", meals, name="meals"),
]
