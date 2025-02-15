from fastapi import APIRouter, HTTPException
from database.services import employee as EmployeeService
from database.utils import get_db
from pydantic import BaseModel, Field


router = APIRouter()

class EmployeeCreateRequest(BaseModel):
    nome: str = Field(..., example="The Great Gatsby")
    telefone: str = Field(..., example="85-123456789")
    id_library: int = Field(..., example=2)


@router.post("/create/employee/", response_class=dict)
def create_employee(employee_data: EmployeeCreateRequest):
    conn = get_db()
    employee = EmployeeService.EmployeeService(conn).create(
        nome = employee_data.nome,
        telefone = employee_data.telefone,
        id_library = employee_data.id_library
    )
    if employee is None:
        raise HTTPException(status_code=400, detail="Failed to create book")
    return {"message": "Book created successfully", "employee": employee}