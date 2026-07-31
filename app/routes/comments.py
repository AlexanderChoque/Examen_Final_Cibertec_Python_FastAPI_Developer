from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas import schemas
from app.repositories.repository import BaseRepository

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post("/", response_model=schemas.CommentResponse, status_code=status.HTTP_201_CREATED)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    if not BaseRepository.get_user(db, comment.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    if not BaseRepository.get_post(db, comment.post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return BaseRepository.create_comment(db=db, comment=comment)

@router.get("/", response_model=List[schemas.CommentResponse])
def read_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return BaseRepository.get_comments(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.CommentResponse)
def read_comment(id: int, db: Session = Depends(get_db)):
    db_comment = BaseRepository.get_comment(db, comment_id=id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.put("/{id}", response_model=schemas.CommentResponse)
def update_comment(id: int, comment: schemas.CommentUpdate, db: Session = Depends(get_db)):
    db_comment = BaseRepository.update_comment(db, comment_id=id, comment_update=comment)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.delete("/{id}", response_model=schemas.CommentResponse)
def delete_comment(id: int, db: Session = Depends(get_db)):
    db_comment = BaseRepository.delete_comment(db, comment_id=id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment