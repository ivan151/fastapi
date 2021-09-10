from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
from config import config
from database import get_db
from models.login import Login
from models.token import Token
from services.hashing import authenticate_user
from services.token import create_access_token, credentials_exception
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

router = APIRouter(
    tags=["Authentication"]
)


class Settings(BaseModel):
    authjwt_secret_key: str = config.token.secret_key
    authjwt_algorithm: str = config.token.algorithm
    authjwt_access_token_expires = config.token.access_token_expire_minutes


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise credentials_exception
    else:
        access_token_expires = timedelta(minutes=config.token.access_token_expire_minutes)
        print(access_token_expires)
        access_token = create_access_token(
            data={"sub": user.login}, expires_delta=access_token_expires)
        print(access_token)
        return {"access_token": access_token, "token_type": "bearer"}


@router.post('/login')
def login(login: Login, authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, login.username, login.password)
    if not user:
        raise credentials_exception
    else:
        # Use create_access_token() and create_refresh_token() to create our
        # access and refresh tokens
        access_token = authorize.create_access_token(subject=user.login)
        refresh_token = authorize.create_refresh_token(subject=user.login)
        return {"access_token": access_token, "refresh_token": refresh_token}


@router.post('/refresh')
def refresh(authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    authorize.jwt_refresh_token_required()

    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@router.get('/protected')
def protected(authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    current_user = authorize.get_jwt_subject()
    return {"user": current_user}
