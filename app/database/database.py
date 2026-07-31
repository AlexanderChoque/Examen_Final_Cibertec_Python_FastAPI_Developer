from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Crear el motor de conexión utilizando la URL del archivo config.py
engine = create_engine(
    settings.database_url, connect_args={"check_same_thread": False}
)

# Fábrica de sesiones para las peticiones a la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base declarativa para definir los modelos ORM
Base = declarative_base()

# Dependencia para obtener la sesión de base de datos en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()