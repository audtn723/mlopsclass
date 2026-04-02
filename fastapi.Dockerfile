FROM python:3.11.6-slim-bullseye

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && pip install --no-cache-dir fastapi uvicorn pydantic catboost \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host=0.0.0.0", "--port=8000", "--app-dir", "/app/"]
