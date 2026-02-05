from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role_id: int


class UserCreate(UserBase):
    password: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role_id: int
    created_at: date

    class Config:
        from_attributes = True
