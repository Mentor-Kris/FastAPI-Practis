from fastapi import FastAPI,status,HTTPException
app=FastAPI()
@app.post("/user",status_code=status.HTTP_201_CREATED)
def get_user():
    return {
        "message":"User created"
    }
@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {
        "id":user_id,
        "name":"krishna"
    }