from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from typing_extensions import Annotated

class SignupDetails(BaseModel):
    username: Annotated[str, Form()]
    firstname: Annotated[str, Form()]
    lastname: Annotated[str, Form()]
    email: Annotated[str, Form()]
    password: Annotated[str, Form()]


class LoginDetails(BaseModel):
    username: Annotated[str, Form()]
    password: Annotated[str, Form()]



class Blog(BaseModel):
    article_no:int
    uname: str
    author: str
    email: str
    language:str
    
class Blogpost(BaseModel):
    author:str
    title:str
    content:str
    