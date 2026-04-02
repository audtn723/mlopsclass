FROM python:3.11.6-slim-bullseye

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && pip install --no-cache-dir pandas sqlalchemy psycopg2-binary requests \
 && rm -rf /var/lib/apt/lists/*

CMD ["python3", "app.py"]
