from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
students=[]
class Student(BaseModel):
    id:int 
    name:str
    age:int
    city:str
@app.post("/student/{student_id}") 
def post_student(student_id:int,student:Student):
    students.append(student)
    return {
        "student":students 
    }
@app.get("/student")
def get_student():
    return {
        "student":students
    }
@app.get("/student/{student_id}")
def get_student(student_id:int):
    for student in students:
        if student.id==student_id:
            return {
                "student":students
            }
@app.put("/student/{student_id}")
def update_student(student_id:int,update_student:Student):
    for index,student in enumerate(students):
        if student.id==student_id:
            students[index]=student
        return {
            "message":"user updated",
            "updated_student":update_student
        }            
@app.delete("/student/{student_id}") 
def delete_student(student_id:int):
    for index,student in enumerate(students):
        if student.id==student_id:
            students.pop(index)
    return {
        "message":"student deleted sucessfully",
        
    }
    return {
        "error":"student can not deleted"
    }       