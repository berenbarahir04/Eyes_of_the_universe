# Utilizar una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt (o el que utilices para las dependencias)
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Copiar todo el código fuente a la carpeta de trabajo
COPY . .

# Exponer el puerto en el que correrá la app (por defecto, Flask usa el 5000)
EXPOSE 5000

ENV FLASK_APP=main.py

# Comando para ejecutar la aplicación
CMD ["flask", "--app", "src/main", "run", "--host=0.0.0.0"]
