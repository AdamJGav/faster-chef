from django.db import migrations


SAMPLE_RECIPES = [
    {
        "name": "Lemon Herb Chicken Bowls",
        "description": "A fresh weeknight bowl with herby chicken, rice, and bright lemon.",
        "ingredients": [
            ("chicken breast", "2", "pieces", "Cut into bite-sized pieces"),
            ("rice", "1", "cup", "Uncooked"),
            ("lemon", "1", "", "Zest and juice"),
            ("olive oil", "1", "tablespoon", ""),
            ("dried oregano", "1", "teaspoon", ""),
        ],
        "steps": [
            (
                1,
                "Rinse the rice and add it to a saucepan with 2 cups of water.",
                "Bring to a boil, then cover and simmer until tender.",
                20,
                "PREP",
            ),
            (
                2,
                "Season the chicken with lemon zest, oregano, salt, and pepper.",
                "Let it sit while the rice cooks.",
                5,
                "PREP",
            ),
            (
                3,
                "Heat the olive oil in a pan and cook the chicken until browned and cooked through.",
                "Finish with lemon juice.",
                10,
                "COOK",
            ),
            (
                4,
                "Serve the chicken over rice.",
                "Add any salad vegetables you have on hand.",
                2,
                "PREP",
            ),
        ],
    },
    {
        "name": "Chickpea Coconut Curry",
        "description": "A comforting plant-based curry with chickpeas, spinach, and coconut milk.",
        "ingredients": [
            ("chickpeas", "2", "400 g cans", "Drained and rinsed"),
            ("coconut milk", "1", "400 ml can", ""),
            ("baby spinach", "2", "cups", ""),
            ("onion", "1", "medium", "Diced"),
            ("curry powder", "2", "teaspoons", ""),
        ],
        "steps": [
            (
                1,
                "Dice the onion and rinse the chickpeas.",
                "Gather the remaining ingredients before cooking.",
                5,
                "PREP",
            ),
            (
                2,
                "Cook the onion in a little oil until softened, then stir in the curry powder.",
                "Keep stirring so the spices do not catch.",
                5,
                "COOK",
            ),
            (
                3,
                "Add the chickpeas and coconut milk, then simmer gently.",
                "Stir occasionally until the sauce thickens slightly.",
                15,
                "COOK",
            ),
            (
                4,
                "Fold in the spinach until just wilted.",
                "Season to taste and serve with rice.",
                3,
                "COOK",
            ),
        ],
    },
    {
        "name": "Tomato Basil Pasta",
        "description": "Simple pasta tossed with garlicky tomatoes and fresh basil.",
        "ingredients": [
            ("pasta", "250", "g", ""),
            ("cherry tomatoes", "300", "g", "Halved"),
            ("garlic", "2", "cloves", "Finely sliced"),
            ("fresh basil", "1", "handful", "Torn"),
            ("olive oil", "2", "tablespoons", ""),
        ],
        "steps": [
            (
                1,
                "Bring a large pot of salted water to the boil.",
                "Prepare the tomatoes and garlic while it heats.",
                8,
                "PREP",
            ),
            (
                2,
                "Cook the pasta according to the packet instructions.",
                "Reserve a mug of pasta water before draining.",
                10,
                "COOK",
            ),
            (
                3,
                "Warm the olive oil and gently cook the garlic, then add the tomatoes.",
                "Cook until the tomatoes soften and release their juices.",
                8,
                "COOK",
            ),
            (
                4,
                "Toss the drained pasta with the tomato sauce and basil.",
                "Add a splash of pasta water if the sauce needs loosening.",
                2,
                "PREP",
            ),
        ],
    },
]


def add_sample_recipes(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Recipe = apps.get_model("core", "Recipe")
    Ingredient = apps.get_model("core", "Ingredient")
    Step = apps.get_model("core", "Step")

    for sample in SAMPLE_RECIPES:
        recipe, created = Recipe.objects.using(db_alias).get_or_create(
            name=sample["name"],
            defaults={"description": sample["description"]},
        )
        if not created:
            continue

        Ingredient.objects.using(db_alias).bulk_create(
            [
                Ingredient(
                    recipe_id=recipe.pk,
                    name=name,
                    quantity=quantity,
                    unit=unit,
                    notes=notes,
                )
                for name, quantity, unit, notes in sample["ingredients"]
            ]
        )
        Step.objects.using(db_alias).bulk_create(
            [
                Step(
                    recipe_id=recipe.pk,
                    order=order,
                    instruction=instruction,
                    additional_info=additional_info,
                    duration=duration,
                    type=step_type,
                )
                for (
                    order,
                    instruction,
                    additional_info,
                    duration,
                    step_type,
                ) in sample["steps"]
            ]
        )


def remove_sample_recipes(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Recipe = apps.get_model("core", "Recipe")
    Recipe.objects.using(db_alias).filter(
        name__in=[sample["name"] for sample in SAMPLE_RECIPES]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_step_additional_info_step_duration_step_type"),
    ]

    operations = [
        migrations.RunPython(add_sample_recipes, remove_sample_recipes),
    ]
