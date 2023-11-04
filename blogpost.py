from fastapi import FastAPI
from schemas import Blog,Blogpost,LoginDetails
import csv

app = FastAPI()




@app.get("/")
def home():
    return 'welcome'


@app.get("/blogpost")
async def get_all_blogposts():
    with open("blogpost.csv","r") as file:
        reader = csv.reader(file)
        all_blogs = []
        for row in reader:
            all_blogs.append(row)
    return all_blogs


@app.get("/blogpost{title}")
async def get_blogposts_by_title(title:str):
     with open("blogpost.csv","r") as file:
        reader = csv.reader(file)
        for line in reader:
            if line[1] == title:
                return {"message":"blogpost found","content":[line[0],line[1],line[2]]}
        return "blogpost not found, verify the title"



# @app.post("/blog/blogpost(add)")
# async def add_blogpost(author:str,title:str,content:str):
#     with open("blogpost.txt","a",newline="") as writeup:
#         writeup.write(author),writeup.write("\n"),writeup.writelines(title),
#         writeup.write("\n"),writeup.writelines(content),writeup.write("\n")
#         return [author,title]


@app.post("/blog/post-blogpost")
async def add_blogpost(login:LoginDetails,blogpost:Blogpost):
    with open("users.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if login.username not in row[0] and login.password in row[4]:
                return {"message":"User not loggedin"}
    with open("blogpost.csv","a",newline="") as writeup:
       writer = csv.writer(writeup)
       writer.writerow([blogpost.author,blogpost.title,blogpost.content])
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
    
    

@app.put("/blog/edit-blogpost")
async def edit_blogpost(blogpost:Blogpost):
    with open("blogpost.csv","r") as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
    with open("blogpost.csv","w",newline="") as file:
        writer = csv.writer(file)
        for index, row in enumerate(rows):
            if blogpost.title != row[1]:
                return {"error":"Blogpost title not found"}
            writer.writerow([blogpost.author,blogpost.title,blogpost.content])
            return {"message":"sucessfully updated"}

