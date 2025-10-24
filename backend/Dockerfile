# 1. Basisimage met Python 3.12
FROM python:3.12-slim

# 2. Werkomgeving in de container
WORKDIR /app

# 3. Kopieer requirements en installeer dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopieer de rest van de backend code
COPY . .


EXPOSE 8000

# 6. Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

