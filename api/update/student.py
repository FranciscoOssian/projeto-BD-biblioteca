from fastapi import APIRouter, HTTPException
from database.services import student as StudentService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/student/{id}")
def update_student(age:int, school:str):
    conn = get_db()
    student = StudentService.StudentService(conn).update(age, school)
    if student is None:
        raise HTTPException(status_code=404, detail="Student não encontrado")
    return student