from fastapi import APIRouter, HTTPException
from database.services import employee as EmployeeService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/employee/{id}")
def update_employee(id:int, nome:str, telefone:str, id_library:int):
    conn = get_db()
    updated = EmployeeService.EmployeeService(conn).update(id, nome, telefone, id_library)
    if updated is None:
        raise HTTPException(status_code=400, detail="Employee não atualizado")
    return {"message": "Book updated successfully", "book": updated}