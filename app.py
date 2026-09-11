from fastapi import FastAPI
app=FastAPI()
@app.get("/movie/{movie_id}")
def get_movie(movie_id:int,language: str,premium: bool):
    if movie_id !=10:
        return {
            "error":"404 movie not found"
        }
    price=300
    if premium==True:
        price+=100
        return {
            "movie_id":movie_id,
            "language":language,
            "price":price,
            "preminm":premium 
        }