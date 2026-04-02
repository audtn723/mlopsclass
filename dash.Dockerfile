FROM python:3.11.6-slim-bullseye

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && pip install --no-cache-dir dash plotly psycopg2-binary pandas numpy sqlalchemy \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 8050

CMD ["python3", "app_run.py"]
