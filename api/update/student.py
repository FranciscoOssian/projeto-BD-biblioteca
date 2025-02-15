from fastapi import APIRouter, HTTPException
from database.services import student as StudentService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/student/{id}")
def update_student(id:int, age:int, school:str):
    conn = get_db()
    updated = StudentService.StudentService(conn).update(id, age, school)
    if updated is None:
        raise HTTPException(status_code=400, detail="Student não atualizado")
    return {"message": "Book updated successfully", "book": updated}