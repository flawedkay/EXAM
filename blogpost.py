from fastapi import FastAPI,APIRouter
from schemas import Blog,Blogpost,LoginDetails
import csv

app = APIRouter()




@app.get("/")
def home():
    return 'welcome'

#To get all blogpost
@app.get("/blogpost")
async def get_all_blogposts():
    with open("blogpost.csv","r") as file:
        reader = csv.reader(file)
        all_blogs = []
        for row in reader:
            all_blogs.append(row[0],row[1],row[2])
    return all_blogs

#To get blogpost content by inputing the title
@app.get("/blogpost{title}")
async def get_blogposts_by_title(title:str):
     with open("blogpost.csv","r") as file:
        reader = csv.reader(file)
        for line in reader:
            if line[1] == title:
                return {"message":"blogpost found","content":[line[0],line[1],line[2]]}
        return "blogpost not found, verify the title"



# To publish or post a blogpost
@app.post("/blog/post-blogpost")
async def add_blogpost(login:LoginDetails,blogpost:Blogpost):
    # Authentifying that only users that are signed up that can post
    with open("users.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if login.username in row[0] and login.password in row[4]:
                continue
            else:
                return {"message":"User not loggedin"}
    # If User is on the signed up list, user can then post to csv
    with open("blogpost.csv","a",newline="") as writeup:
       writer = csv.writer(writeup)
       writer.writerow([blogpost.author,blogpost.title,blogpost.content,login.password]) # The password column is a form of ID authentification for editing.
    return {"message":"blogpost published","Blogpost title":blogpost.title}


# @app.put("/blog/edit-blogpost")
# async def edit_blogpost(blogpost:Blogpost):
#     with open("blogpost.csv","r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if blogpost.title == row[1]:
#                 return {"error":"Blogpost title not found"}        
#     with open("blogpost.csv","w") as file:
#         writer = csv.writer(file)
#         writer.writerow([blogpost.author,blogpost.title,blogpost.content])
#         return {"message":"Blogpost updated successfully","data":blogpost}
    
    
# To edit a blogpost
@app.put("/blog/edit-blogpost{blogpost.title}")
async def edit_blogpost(password:str,blogpost:Blogpost):
    with open("blogpost.csv","r") as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
# To first ensure only the author can edit the particular post        
        for index, row in enumerate(rows):
            if password == row[3]:
                continue
            else:
                return {"message":"Wrong password, only author can edit blogpost"}
    # Updating the blogpost
    with open("blogpost.csv","w",newline="") as file:
        writer = csv.writer(file)
        for index, row in enumerate(rows):
            if blogpost.title == row[1]:
                writer.writerow([blogpost.author,blogpost.title,blogpost.content,password])
            else:
                return {"error":"Blogpost title not found"}
        return {"message":"sucessfully updated"}


@app.delete("/blog/delete-blogpost{blogtitle}")
async def delete_blogpost(password:str,blogtitle:str):
    with open("blogpost.csv","r") as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
    # To first ensure only the author can delete the particular post
        for index, row in enumerate(rows):
            if password == row[3]:
                continue
            else:
                return {"message":"Wrong password, only author can delete blogpost"} 
    # delete the blogpost
    with open("blogpost.csv","w",newline="") as file:
        writer = csv.writer(file)
        for index, row in enumerate(rows):
            print(row)                  
            if blogtitle == row[1]:
                continue
            else:
                writer.writerow(row[index])
                return {"error":"Blogpost title not found"}
        return {"message":"sucessfully deleted"}
