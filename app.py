from fastapi import FastAPI
app=FastAPI()
@app.get("/ticket/{ticket_id}")
def get_ticket(ticket_id:int,type:str,event:str,vip:bool):
    if ticket_id!=1:
        return {
            "error":"404 ticket not found"
        }
    price=200
    if vip==True:
        price+=300
    return {
        "message":"ticket get sucessfully",
        "ticket_id":ticket_id,
        "type":type,
        "event": "Concert",
        "price":price,
        "vip":vip
    }    