from pydantic import BaseModel

class UserModel(BaseModel):
    email: str
    name: str
    password: str
    email: str

class UserCreate(UserModel):
    password: str

class User(UserModel):
    id: int
    class Config:
        orm_mode = True
