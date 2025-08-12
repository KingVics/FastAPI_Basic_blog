from pydantic import BaseModel
from typing import Optional, List


class BlogBase(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    

class Blog(BlogBase):    
    class Config():
        orm_mode = True
    
class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: str
    blogs:  List[Blog] = []
    class Config():
        orm_mode = True
        
class ShowBlog(Blog):
    creator: ShowUser
    class Config():
        orm_mode = True
        

class Auth(BaseModel):
    email: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None