from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
from typing import Optional
from .config import settings


pwd_context = CryptContext(schemes=["bycrypt"], deprecated = "auto")


def hash_password(password: str)-> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRY_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)