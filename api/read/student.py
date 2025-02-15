from fastapi import APIRouter, HTTPException
from database.services import student as StudentService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/student/{id}")
def get_student(id: int):
    print(id)
    conn = get_db()
    student = StudentService.StudentService(conn).get(id)
    if student is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return student