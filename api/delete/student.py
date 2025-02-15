from fastapi import APIRouter, HTTPException
from database.services import student as StudentService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/student/{id}")
def delete_student(id:int):
    conn = get_db()
    deleted = StudentService.StudentService(conn).delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student não encontrado")
    return {"message": "Book deleted successfully"}