from django import forms

from core.models import Recipe
from core.models import Ingredient
from core.models import Step

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description"]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "quantity", "unit", "notes"]

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ["order"]