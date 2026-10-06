FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SQLITE_PATH=/app/data/db.sqlite3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && mkdir -p /app/data \
    && useradd --create-home --uid 10001 app \
    && chown -R app:app /app

COPY --chown=app:app . .

USER app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
