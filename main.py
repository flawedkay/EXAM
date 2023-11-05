from fastapi import FastAPI,APIRouter,Response

from blogpost import app as Blog_router
from User import app as User_router

app = FastAPI()

app.include_router(Blog_router, prefix="/Blogs", tags=["Blogs"])
app.include_router(User_router, prefix="/Users", tags=["Users"])
    


@app.get("/")
def home():
    return "Welcome to my Blogsite"

@app.get("/about")
def about():
    return "This application is a blog website that lets users read, create, update and delete blogpost"

@app.get("/contact")
def contact():
    return "You can contact the builder on Github, username: flawedkay"