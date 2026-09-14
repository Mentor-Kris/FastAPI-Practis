import sqlite3
from fastapi import FastAPI
app=FastAPI()
conn=sqlite3.connect("k.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute(""" create table if not exists todo(
id,
title text,
completed text)
""")
conn.commit()

@app.get("/")
def home():
    return {
        "message":"sqlite connected fine"
    }
