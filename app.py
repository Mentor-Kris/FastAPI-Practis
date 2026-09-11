from fastapi import FastAPI

app=FastAPI()
@app.get("/product/{product_id}")
def get_product(product_id:int,discount: bool,currency: str):
    price =50000
    if discount:
        price=price-(price*10/100)
    return {
        "message":"product get sucessfully",
        "product_id":product_id,
        "price":price,
        "discount_applied": discount,
        "currency":currency
    }