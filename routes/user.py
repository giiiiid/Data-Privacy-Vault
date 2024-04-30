from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.config import get_db
from config.schema import UserInModel, UserOutModel
from models.models import User
from config.config import encrypt_data, decrypt_data


user = APIRouter()


@user.post("/user/register", response_model=UserOutModel)
async def tokenize(user: UserInModel, db: Session = Depends(get_db) ):
    username, username_tag = encrypt_data(user.username)
    email, email_tag = encrypt_data(user.email)
    password, password_tag = encrypt_data(user.password)

    new_user = User(username=username, email=email, password=password,
                    username_tag=username_tag, email_tag=email_tag, password_tag=password_tag
                    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@user.post("/detokenize")
async def detokize(user:UserInModel, db: Session = Depends(get_db)):
    # username = db.query(User).filter(user.username == decrypt_data(User.username, User.username_tag)).first()
    # email = db.query(User).filter(user.email == decrypt_data(User.email, User.email_tag)).first()
    # password = db.query(User).filter(user.password == decrypt_data(User.password, User.password_tag)).first()

    user = db.query(User).filter(
        user.username == decrypt_data(User.username, User.username_tag),
        user.email == decrypt_data(User.email, User.email_tag),
        user.password == decrypt_data(User.password, User.password_tag)
    ).first()

    if user.username and user.email and not user.password:
        return {
            "id": user.id,
            "data": {
                "username": {
                    "found": True,
                    "value": user.username
                },
                "email": {
                    "found": True,
                    "value": user.email
                },
                "password": {
                    "found": False, 
                    "value": " "
                }
            }
        }
    
    elif user.username and user.password and not user.email:
        return {
            "id": user.id,
            "data": {
                "username": {
                    "found": True,
                    "value": user.username
                },
                "email": {
                    "found": False,
                    "value": " "
                },
                "password": {
                    "found": True, 
                    "value": user.password
                }
            }
        }
    
    elif user.email and user.password and not user.username:
        return {
            "id": user.id,
            "data": {
                "username": {
                    "found": False,
                    "value": " "
                },
                "email": {
                    "found": True,
                    "value": user.email
                },
                "password": {
                    "found": True, 
                    "value": user.password
                }
            }
        }
    else:
        raise HTTPException(
            status_code= 404,
            detail= "User not found"
        )