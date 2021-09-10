from fastapi import Depends, FastAPI, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import and_
from pydantic.error_wrappers import ValidationError

import models
import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(schemas.User).filter(schemas.User.login == username).first()
    if user:
        user_p = models.user.User.from_orm(user)
        print(f"{user_p.json()}")
        print(verify_password(password, user_p.password_hash))
        if not verify_password(password, user_p.password_hash):
            return None
        else:
            return user_p
    else:
        raise status.HTTP_404_NOT_FOUND
