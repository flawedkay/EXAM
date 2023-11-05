from fastapi import FastAPI, File, UploadFile, Form,APIRouter
from schemas import SignupDetails,LoginDetails,UserDetails
import csv

app = APIRouter()

@app.get("/")
def home():
    return {"message": "Welcome to my Upload API"}

# Form for Signup route
@app.post("/signup")
async def signup(signup:SignupDetails):
    with open("users.csv","r") as file:
        reader = csv.reader(file)
# conditional statement to avoid multiple registration
# with same email, and also to achieve unique username
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

# To edit user information
@app.put("/edit-user-details{userinfo.username}")
async def edit_user_info(user:str,userinfo:UserDetails):
    with open("users.csv","r") as file:
        reader = csv.reader(file)
# conditional statement to confirm user is already signed up
        for row in reader:
            if user in row[0]:
                with open("users.csv","a",newline="") as file:
                    writer = csv.writer(file)
                    row[1] = ['firsname',userinfo.firstname]
                    row[2] = ['lastname',userinfo.lastname]
                    row[4] = ['password',userinfo.password]
                    writer.writerow([row[1],row[2],row[4]])
                return {"message":f"{user}, you have successfully updated his details","details":
                        {"username": user, "firstname": userinfo.firstname, "lastname": userinfo.lastname}}