# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/")
# def get():
#     return {
#         "message":"Hello FastAPI"
#     }
from fastapi import FastAPI
app=FastAPI()
@app.get("/user")
def get_user(limit:int,active:bool):
    return {
        "message":"query parameter",
        "Limit":limit,
        "Active":active
                } 