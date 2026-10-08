from django.contrib import admin

from core.models import Ingredient, Recipe, Step


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class StepInline(admin.TabularInline):
    model = Step
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name", "description")
    inlines = (IngredientInline, StepInline)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "recipe", "quantity", "unit")
    list_filter = ("recipe",)
    search_fields = ("name", "recipe__name")


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("recipe", "order", "type", "duration")
    list_filter = ("type", "recipe")
    search_fields = ("instruction", "recipe__name")
