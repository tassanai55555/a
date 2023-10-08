FROM python:3.9-alpine
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

# Install necessary system-level dependencies
RUN apk update && apk add --no-cache build-base python3-dev libffi-dev postgresql-client

# Install Python dependencies
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["daphne", "core.asgi:application", "0.0.0.0:8000"]
