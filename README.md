# Examen_Final_Cibertec_Python_FastAPI_Developer
API REST desarrollada con **FastAPI**, **SQLAlchemy ORM** (SQLite), y una arquitectura limpia por capas (Repository y Service Layer).

## Descripción del proyecto
El objetivo de esta aplicación es proveer un backend robusto y escalable para la gestión de usuarios, publicaciones (posts) y comentarios (comments), cumpliendo estrictamente con principios de código limpio, variables de entorno, control de versiones y documentación automática.

## Instalación y ejecución utilizando UV

Este proyecto utiliza **UV** para la gestión ultrarrápida de dependencias y entornos virtuales. Sigue estos pasos para replicarlo localmente:

Crear el entorno virtual e instalar dependencias con UV:
uv venv
source .venv/Scripts/activate  # En Windows (Git Bash / PowerShell)
uv sync

Configurar las variables de entorno:
# Duplica el archivo .env.example y nómbralo .env.
# Rellena las variables requeridas (SECRET_KEY, DATABASE_URL, etc.).

Ejecutar el servidor de desarrollo:
uvicorn app.main:app --reload

Acceder a la documentación automática:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc