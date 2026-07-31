from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas import schemas
from app.services.service import BusinessService

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=schemas.PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = BusinessService.register_post(db=db, post=post)
    if not db_post:
        raise HTTPException(status_code=404, detail="User not found")
    return db_post

@router.get("/", response_model=List[schemas.PostResponse])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return BusinessService.fetch_posts(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.PostResponse)
def read_post(id: int, db: Session = Depends(get_db)):
    db_post = BusinessService.fetch_post_by_id(db, post_id=id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    db_post = BusinessService.modify_post(db, post_id=id, post_update=post)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.delete("/{id}", response_model=schemas.PostResponse)
def delete_post(id: int, db: Session = Depends(get_db)):
    db_post = BusinessService.remove_post(db, post_id=id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post