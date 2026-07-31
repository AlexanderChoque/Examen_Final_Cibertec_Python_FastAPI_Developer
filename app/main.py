from fastapi import FastAPI
from app.database.database import engine
from app.database import models
from app.routes import users, posts, comments

# Crear las tablas en la base de datos automáticamente al iniciar
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Examen Final FastAPI",
    description="API REST desarrollada con FastAPI, SQLAlchemy y SQLite",
    version="1.0.0"
)

# Incluir los routers de los CRUDs
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)

@app.get("/")
def root():
    return {"message": "Bienvenido al examen final de FastAPI"}