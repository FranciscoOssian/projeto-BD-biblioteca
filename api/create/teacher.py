from fastapi import APIRouter, HTTPException
from database.services import teacher as TeacherService
from database.utils import get_db

router = APIRouter()
    
@router.post("/create/teacher/{id}")
def create_teacher(email:str, materia:str):
    conn = get_db()
    teacher = TeacherService.TeacherService(conn).create(email, materia)
    if teacher is None:
        raise HTTPException(status_code=400, detail="Failed to create teacher")
    return teacher