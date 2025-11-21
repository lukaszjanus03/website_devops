# Baza: lekki Python
FROM python:3.9-slim

WORKDIR /app

# Instalujemy Flask i requests
RUN pip install flask requests flask-cors

# Kopiujemy nasz skrypt
COPY weather.py .

# Uruchamiamy aplikację
CMD ["python", "weather.py"]
