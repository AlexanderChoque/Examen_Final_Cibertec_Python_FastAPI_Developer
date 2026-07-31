from sqlalchemy.orm import Session
from app.database import models
from app.schemas import schemas

class BaseRepository:
    # --- USERS ---
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate):
        db_user = models.User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
        db_user = BaseRepository.get_user(db, user_id)
        if not db_user:
            return None
        update_data = user_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        db_user = BaseRepository.get_user(db, user_id)
        if not db_user:
            return None
        db.delete(db_user)
        db.commit()
        return db_user

    # --- POSTS ---
    @staticmethod
    def get_posts(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Post).offset(skip).limit(limit).all()

    @staticmethod
    def get_post(db: Session, post_id: int):
        return db.query(models.Post).filter(models.Post.id == post_id).first()

    @staticmethod
    def create_post(db: Session, post: schemas.PostCreate):
        db_post = models.Post(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    def update_post(db: Session, post_id: int, post_update: schemas.PostUpdate):
        db_post = BaseRepository.get_post(db, post_id)
        if not db_post:
            return None
        update_data = post_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    def delete_post(db: Session, post_id: int):
        db_post = BaseRepository.get_post(db, post_id)
        if not db_post:
            return None
        db.delete(db_post)
        db.commit()
        return db_post

    # --- COMMENTS ---
    @staticmethod
    def get_comments(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Comment).offset(skip).limit(limit).all()

    @staticmethod
    def get_comment(db: Session, comment_id: int):
        return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

    @staticmethod
    def create_comment(db: Session, comment: schemas.CommentCreate):
        db_comment = models.Comment(**comment.dict())
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        return db_comment

    @staticmethod
    def update_comment(db: Session, comment_id: int, comment_update: schemas.CommentUpdate):
        db_comment = BaseRepository.get_comment(db, comment_id)
        if not db_comment:
            return None
        update_data = comment_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_comment, key, value)
        db.commit()
        db.refresh(db_comment)
        return db_comment

    @staticmethod
    def delete_comment(db: Session, comment_id: int):
        db_comment = BaseRepository.get_comment(db, comment_id)
        if not db_comment:
            return None
        db.delete(db_comment)
        db.commit()
        return db_comment