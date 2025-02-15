from fastapi import APIRouter, HTTPException
from database.services import employee as EmployeeService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/employee/{id}")
def get_employee(id: int):
    print(id)
    conn = get_db()
    employee = EmployeeService.EmployeeService(conn).get(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Funcionario não encontrado")
    return employee