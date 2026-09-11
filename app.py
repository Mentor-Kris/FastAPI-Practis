from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Product(BaseModel):
    name: str
    price: int
    secret_code: str
class UserResponse(BaseModel):
    name:str
    price:int
@app.get("/product",response_model=UserResponse)
def get_product():
    return {
       "name":"leptop",
       "price":60000,
       "secret_code":"ABC123"
    }    