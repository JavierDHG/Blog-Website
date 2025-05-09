# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt .

# Instala dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["gunicorn", "blog_website.wsgi:application", "--bind", "0.0.0.0:8000"]