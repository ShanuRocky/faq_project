FROM python:3.12

WORKDIR /app

# Ensure the destination is correct
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
