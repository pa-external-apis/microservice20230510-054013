
FROM python:3.9-slim-buster

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py .
COPY templates templates

CMD ["python", "app.py"]

