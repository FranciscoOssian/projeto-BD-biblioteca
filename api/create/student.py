from fastapi import APIRouter, HTTPException
from database.services import student as StudentService
from database.utils import get_db

router = APIRouter()
    
@router.post("/create/student/{id}")
def create_student(age:int, school:str):
    conn = get_db()
    student = StudentService.StudentService(conn).create(age, school)
    if student is None:
        raise HTTPException(status_code=400, detail="Failed to create student")
    return student