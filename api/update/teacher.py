from fastapi import APIRouter, HTTPException
from database.services import teacher as TeacherService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/teacher/{id}")
def update_teacher(email:str, materia:str):
    conn = get_db()
    teacher = TeacherService.TeacherService(conn).update(email, materia)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher não encontrado")
    return teacher