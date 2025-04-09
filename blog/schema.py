from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(Blog):
    title : str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True

    
class Login(BaseModel):
    username: str
    password: str
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None










