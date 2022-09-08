from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """
    Campos del usuario
    """
    id: Optional[str]
    name: str
    email: EmailStr
    password: str


class UserAuth(BaseModel):
    """
    Campos del usuario para la autentificación
    """
    email: EmailStr
    password: str
