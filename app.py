from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
students=[]
class Student(BaseModel):
    id:int
    name:str
    age:int
    college:str
@app.post("/student")
def create_student(student:Student):
    students.append(student)
    return {
        "message":"Student created sucessfully",
        "Student":students
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
                "student":student,
                
            }
@app.put("/student/{student_id}")
def update_student(student_id:int,student_update:Student):
    for index,student in enumerate(students):
        if student.id==student_id:
            students[index]=student
        return {
            "message":"student updated sucessfully",
            "student":student 
        }    
@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    for index,student in enumerate(students):
        if student.id==student_id:
            students.pop(index)
        return {
            "message":"student deleted sucessfully"
        }    
