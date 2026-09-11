# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/")
# def get():
#     return {
#         "message":"Hello FastAPI"
#     }
# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/user")
# def get_user(limit:int,active:bool):
#     return {
#         "message":"query parameter",
#         "Limit":limit,
#         "Active":active
#                 } 
# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# class User(BaseModel):
#     name:str
#     age:int
# @app.post("/user")
# def creat_user(user:User):
#     return {
#         "message":"User created",
#         "data":user 
#     }    
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Address(BaseModel):
    state:str
    city:str
    pincode:int 
class Student(BaseModel):
    name:str
    age:int
    college:str
    address:Address
@app.post("/user")
def creat_user(user:Student):
    return {
        "message":"User created sucessfully",
        "User":user 
    }        