from fastapi import APIRouter, HTTPException
from database.services import employee as EmployeeService
from database.utils import get_db

router = APIRouter()
    
@router.get("/create/employee/{id}")
def create_employee(nome:str, telefone:str, id_library:int):
    conn = get_db()
    employee = EmployeeService.EmployeeService(conn).create(nome, telefone, id_library)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee não encontrado")
    return employee