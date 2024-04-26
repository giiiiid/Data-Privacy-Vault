from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.config import get_db
from config.schema import UserInModel, UserOutModel
from models.models import User
import re


user = APIRouter()


@user.post("/user/register", response_model=UserOutModel)
async def create_user(user: UserInModel, db: Session = Depends(get_db) ):
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "data": {
            "username": new_user.username,
            "email": new_user.email
        }
    }


@user.post("/user/tokenize")
async def tokenize