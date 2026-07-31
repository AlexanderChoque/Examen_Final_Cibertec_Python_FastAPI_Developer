from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas import schemas
from app.repositories.repository import BaseRepository

router = APIRouter(prefix="/users", tags=["Users"])

@app.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED) # type: ignore
@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return BaseRepository.create_user(db=db, user=user)

@router.get("/", response_model=List[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return BaseRepository.get_users(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.UserResponse)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = BaseRepository.get_user(db, user_id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = BaseRepository.update_user(db, user_id=id, user_update=user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{id}", response_model=schemas.UserResponse)
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = BaseRepository.delete_user(db, user_id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user