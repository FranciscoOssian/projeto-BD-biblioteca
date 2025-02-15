from fastapi import APIRouter, HTTPException
from database.services import employee as EmployeeService
from database.utils import get_db

router = APIRouter()
    
@router.get("/delete/employee/{id}")
def delete_employee(id:int):
    conn = get_db()
    employee = EmployeeService.EmployeeService(conn).delete(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee não encontrado")
    return employee