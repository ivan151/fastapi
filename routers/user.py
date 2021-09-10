from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db
from services.token import credentials_exception, oauth2_scheme, verify_token, get_current_active_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get('/all')
def show_all_users(db: Session = Depends(get_db), ):
    users = db.query(schemas.User).all()
    return users


@router.get("/me", response_model=models.user.User)
async def read_users_me(current_user: models.user.User = Depends(get_current_active_user)):
    return current_user
