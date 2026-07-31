from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

# --- SCHEMAS PARA USER ---
class UserBase(BaseModel):
    given_name: str
    family_name: str
    email: EmailStr
    phone_number: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# --- SCHEMAS PARA POST ---
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostResponse(PostBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# --- SCHEMAS PARA COMMENT ---
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    user_id: int
    post_id: int

class CommentUpdate(BaseModel):
    content: Optional[str] = None

class CommentResponse(CommentBase):
    id: int
    user_id: int
    post_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True