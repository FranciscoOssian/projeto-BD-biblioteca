from fastapi import APIRouter, HTTPException
from database.services import teacher as TeacherService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/teacher/{id}")
def get_teacher(id: int):
    print(id)
    conn = get_db()
    teacher = TeacherService.TeacherService(conn).get(id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher não encontrado")
    return teacher