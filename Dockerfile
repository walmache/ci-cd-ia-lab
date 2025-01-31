FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

#CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.app:app"]
CMD ["gunicorn", "--workers=1", "--threads=4", "--timeout=120", "--bind", "0.0.0.0:8080", "app.app:app"]
