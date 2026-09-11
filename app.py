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
# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# class Address(BaseModel):
#     state:str
#     city:str
#     pincode:int 
# class Student(BaseModel):
#     name:str
#     age:int
#     college:str
#     address:Address
# @app.post("/user")
# def creat_user(user:Student):
#     return {
#         "message":"User created sucessfully",
#         "User":user 
#     }  
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
Book=[]
class Books(BaseModel):
    id:int
    name:str
    author:str
@app.post("/book/{book_id}")
def get_book(book_id:int,book:Books):
    Book.append(book)
    return {
        "message":"book created sucessfully",
        "Book":Book 
    }
@app.get("/book")
def get_book():
    return {
           "Book":Book 
    }
@app.get("/book/{book_id}")
def get_book(book_id:int):
    for book in Book:
        if book.id==book_id:
            return book 
@app.put("/book/{book_id}")
def update_book(book_id:int,update_book:Books):
    for index,book in enumerate(Book):
        if book.id==book_id:
            Book[index]=update_book
        return {
            "message":"data updated",
            "data":update_book 
        }            
@app.delete("/book/{book_id}")
def book_delete(book_id:int):
    for index,book in enumerate(Book):
        if book.id==book_id:
            Book.pop(index)
    return {
        "message":"book delete sucessfully"
    }
    return {
        "error":"book not found"
    }        