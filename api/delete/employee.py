from fastapi import APIRouter, HTTPException
from database.services import employee as EmployeeService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/employee/{id}")
def delete_employee(id:int):
    conn = get_db()
    deleted = EmployeeService.EmployeeService(conn).delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee não encontrado")
    return {"message": "employee deleted successfully"}