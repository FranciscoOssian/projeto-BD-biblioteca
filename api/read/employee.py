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

@router.get("/read/employees")
def get_book_all():
    conn = get_db()
    employees = EmployeeService.EmployeeService(conn).get_all()
    if employees is None:
        raise HTTPException(status_code=404, detail="Employees não encontrados")
    return employees 