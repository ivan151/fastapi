from fastapi import HTTPException, status, Depends
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from typing import Optional
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from config import config
from database import get_db
import models
import schemas
from models.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.token.secret_key,
                             algorithm=config.token.algorithm)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, config.token.secret_key,
                             algorithms=[config.token.algorithm])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
        return token_data
    except JWTError:
        raise credentials_exception


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    print("level1")
    print(token)
    token_data = verify_token(token)
    print("level2")
    user_from_db = db.query(schemas.User).filter(schemas.User.login == token_data.username).first()
    if not user_from_db:
        raise credentials_exception
    return models.user.User.from_orm(user_from_db)


async def get_current_active_user(current_user: models.user.User = Depends(get_current_user)):
    if not current_user.is_bot:
        raise HTTPException(status_code=400, detail="Inactive user")
    print(current_user)
    return current_user
