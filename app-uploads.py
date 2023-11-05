from fastapi import FastAPI, File, UploadFile, Form
from typing_extensions import Annotated
from typing import Optional
from schemas import SignupDetails,LoginDetails
import csv

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my Upload API"}

# Form for Signup route
@app.post("/signup")
async def signup(signup:SignupDetails):
    with open("users.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if signup.username in row[0] or signup.email in row[3]:
                return {"error":"Username taken or User already registered"}
    with open("users.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(signup)
    return {"message":f"{signup.username}, you have successfully signed up","details":
            {"username": signup.username, "firstname": signup.firstname, "lastname": signup.lastname}}
    

# Login route
@app.post("/login")
async def login(login:LoginDetails):
   with open("users.csv","r") as file:
       reader = csv.reader(file)
       for row in reader:
           print(row)
           if login.username in row[0] and login.password in row[4]:
               return {"message":f"{login.username} logged in successfully"}
   return {"message":"User not registered"}

# User Details
@app.post("/user")
async def user(
    age: Annotated[int, Form()],
    name: Annotated[str, Form()],
    DOB: Annotated[str, Form()],
    gender: Annotated[str, Form()],
    nationality: Annotated[str, Form()]
):
    return {"age": age, "name":name, "Date of Birth":DOB}

