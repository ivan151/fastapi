from fastapi import FastAPI, Depends, Response, status, HTTPException
from typing import Optional

import schemas
import uvicorn

from database import get_db
from models.user import User, UserShort
from sqlalchemy.orm import Session
from routers import auth, user

from services.hashing import get_password_hash

app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def index(limit: int, published: bool,
          sort: Optional[str] = None):
    # only get 10 blogs
    if published:
        return {"blogs": f"{limit} published blogs from db"}
    else:
        return {"blogs": f"{limit} unpublished blogs from db"}


@app.get("/about")
def about():
    return {"some": {"data": 2}}


@app.post('/users')
def create_user(user: User, db: Session = Depends(get_db)):
    args = user.dict()
    hashed_pass = get_password_hash(user.password_hash)
    args["password_hash"] = hashed_pass
    new_user = schemas.user.User(**args)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', response_model=UserShort)
def show(id, response: Response, db: Session = Depends(get_db)):
    user = db.query(schemas.user.User).filter(schemas.user.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="user with this id doesn't exist")

    return user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
