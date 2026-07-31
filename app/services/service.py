from sqlalchemy.orm import Session
from app.repositories.repository import BaseRepository
from app.schemas import schemas

class BusinessService:
    # --- USERS ---
    @staticmethod
    def register_user(db: Session, user: schemas.UserCreate):
        return BaseRepository.create_user(db, user)

    @staticmethod
    def fetch_users(db: Session, skip: int = 0, limit: int = 100):
        return BaseRepository.get_users(db, skip, limit)

    @staticmethod
    def fetch_user_by_id(db: Session, user_id: int):
        return BaseRepository.get_user(db, user_id)

    @staticmethod
    def modify_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
        return BaseRepository.update_user(db, user_id, user_update)

    @staticmethod
    def remove_user(db: Session, user_id: int):
        return BaseRepository.delete_user(db, user_id)

    # --- POSTS ---
    @staticmethod
    def register_post(db: Session, post: schemas.PostCreate):
        user = BaseRepository.get_user(db, post.user_id)
        if not user:
            return None
        return BaseRepository.create_post(db, post)

    @staticmethod
    def fetch_posts(db: Session, skip: int = 0, limit: int = 100):
        return BaseRepository.get_posts(db, skip, limit)

    @staticmethod
    def fetch_post_by_id(db: Session, post_id: int):
        return BaseRepository.get_post(db, post_id)

    @staticmethod
    def modify_post(db: Session, post_id: int, post_update: schemas.PostUpdate):
        return BaseRepository.update_post(db, post_id, post_update)

    @staticmethod
    def remove_post(db: Session, post_id: int):
        return BaseRepository.delete_post(db, post_id)

    # --- COMMENTS ---
    @staticmethod
    def register_comment(db: Session, comment: schemas.CommentCreate):
        user = BaseRepository.get_user(db, comment.user_id)
        post = BaseRepository.get_post(db, comment.post_id)
        if not user or not post:
            return None
        return BaseRepository.create_comment(db, comment)

    @staticmethod
    def fetch_comments(db: Session, skip: int = 0, limit: int = 100):
        return BaseRepository.get_comments(db, skip, limit)

    @staticmethod
    def fetch_comment_by_id(db: Session, comment_id: int):
        return BaseRepository.get_comment(db, comment_id)

    @staticmethod
    def modify_comment(db: Session, comment_id: int, comment_update: schemas.CommentUpdate):
        return BaseRepository.update_comment(db, comment_id, comment_update)

    @staticmethod
    def remove_comment(db: Session, comment_id: int):
        return BaseRepository.delete_comment(db, comment_id)