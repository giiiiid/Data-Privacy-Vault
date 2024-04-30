from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    email: str


class UserInModel(UserModel):
    password: str


class UserOutModel(UserModel):
    pass


