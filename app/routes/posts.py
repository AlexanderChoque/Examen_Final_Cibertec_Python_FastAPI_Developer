from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas import schemas
from app.repositories.repository import BaseRepository

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=schemas.PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # Validar que el usuario exista
    if not BaseRepository.get_user(db, post.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return BaseRepository.create_post(db=db, post=post)

@router.get("/", response_model=List[schemas.PostResponse])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return BaseRepository.get_posts(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.PostResponse)
def read_post(id: int, db: Session = Depends(get_db)):
    db_post = BaseRepository.get_post(db, post_id=id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    db_post = BaseRepository.update_post(db, post_id=id, post_update=post)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.delete("/{id}", response_model=schemas.PostResponse)
def delete_post(id: int, db: Session = Depends(get_db)):
    db_post = BaseRepository.delete_post(db, post_id=id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post