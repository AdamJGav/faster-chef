# Faster Chef

A meal planning and prep app built with Python, Django, Jinja2 templates, SQLite, and Tailwind CSS.

## Run with Docker

Build and start the app:

```sh
docker compose up --build
```

Open [http://localhost:8000](http://localhost:8000). Django applies database migrations when the container starts. SQLite data is stored in the `sqlite_data` Docker volume and persists when the container is recreated.

## Django admin

Create an administrator account in the running container:

```sh
docker compose exec web python manage.py createsuperuser
```

Sign in at [http://localhost:8000/admin/](http://localhost:8000/admin/). Recipes, ingredients, and steps are available there; ingredients and steps can also be added inline while editing a recipe.

## Templates

Pages extend `templates/base.jinja`, which includes the shared header and footer. Page-specific content goes in a `{% block content %}`; reusable snippets live in `templates/components/`. The recipe detail page is `templates/recipes/recipe.jinja`.

To stop the app, press `Ctrl+C`; to remove the container while keeping the database, run `docker compose down`.

## Configuration

Compose supports these environment variables:

- `DJANGO_SECRET_KEY`: Django secret key. The default is for local development only.
- `DJANGO_DEBUG`: Enable Django debug mode (`true` or `false`); defaults to `true` in Compose.
- `DJANGO_ALLOWED_HOSTS`: Comma-separated allowed host names; defaults to `localhost,127.0.0.1`.

The starter page uses the Tailwind browser CDN, so it needs an internet connection. For production, compile Tailwind assets locally and use a production-ready Django server instead of `runserver`.
