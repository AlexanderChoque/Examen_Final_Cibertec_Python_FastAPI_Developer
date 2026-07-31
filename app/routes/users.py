from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas import schemas
from app.services.service import BusinessService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return BusinessService.register_user(db=db, user=user)

@router.get("/", response_model=List[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return BusinessService.fetch_users(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.UserResponse)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = BusinessService.fetch_user_by_id(db, user_id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = BusinessService.modify_user(db, user_id=id, user_update=user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{id}", response_model=schemas.UserResponse)
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = BusinessService.remove_user(db, user_id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user