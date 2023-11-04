from fastapi import FastAPI
from pydantic import BaseModel
import csv


app = FastAPI()

class User(BaseModel):
    uname: str
    password: str
    email: str
    firstname: str
    lastname: str



@app.post("/user/")
async def create_user(user:User):
    with open("database.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user.uname,user.password,user.email,user.firstname,user.lastname])
        with open("database.csv","r",newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == user.email:
                 return {"error":"email has been previously registered"}
        return{"message":"User created successfully","data":[user.uname,user.email]}
    

# @app.put("/user{username}")
# async def get_user_by_username_and_password(user):
#     with open("database.csv","r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if row[0] == user.uname and row[1] == user.password:
#                 return Person(id=int(row[0]), name=row[1], age=int(row[2]))
#     return {"message":"person not found"}