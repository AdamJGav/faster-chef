from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, blank=True)
    unit = models.CharField(max_length=50, blank=True)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    class Type(models.TextChoices):
        PREP = "PREP", "Prep"
        COOK = "COOK", "Cook"

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="steps",
    )
    order = models.PositiveIntegerField()
    instruction = models.TextField()
    additional_info = models.TextField()
    duration = models.IntegerField()
    type = models.CharField(max_length=4, choices=Type.choices)

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "order"],
                name="unique_step_order_per_recipe",
            )
        ]

    def __str__(self):
        return f"{self.recipe}: Step {self.order}"
