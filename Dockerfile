# FROM python:3.9

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# #CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.app:app"]
# CMD ["gunicorn", "--workers=1", "--threads=4", "--timeout=120", "--bind", "0.0.0.0:8080", "app.app:app"]

# Usa Python 3.9 como base
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias y actualiza pip
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente
COPY . .

# Asegurar que el modelo existe en la imagen
COPY model/ model/

# Especificar Gunicorn con configuraciones optimizadas
CMD ["gunicorn", "--workers=1", "--threads=4", "--timeout=120", "--bind", "0.0.0.0:8080", "app.app:app"]



