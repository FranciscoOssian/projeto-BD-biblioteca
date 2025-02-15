from fastapi import APIRouter, HTTPException
from database.services import teacher as TeacherService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/teacher/{id}")
def delete_teacher(id:int):
    conn = get_db()
    deleted = TeacherService.TeacherService(conn).delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Teacher não encontrado")
    return {"message": "Book deleted successfully"}