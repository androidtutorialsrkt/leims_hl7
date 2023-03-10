from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()


class Users(BaseModel):
   title:str
   content:str


@app.post("/user_detail") 
def create_user(user:Users):
   print (user.title)
   print (user.content)
   return {"data": user}
 

@app.get("/") 
def getUsers():
   return {"message": "Get All users"}

@app.get("/get_single_user") 
def getSingleUser():
   return {"message": "Get Single User"}
