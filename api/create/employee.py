from fastapi import APIRouter, HTTPException
from api.types.employee import Employee
from database.services import employee as EmployeeService
from database.utils import get_db
from pydantic import BaseModel

router = APIRouter()

class Req(BaseModel):
    employee: Employee

@router.post("/create/employee/")
def create_employee(req: Req):
    conn = get_db()
    done = EmployeeService.EmployeeService(conn).create_employee(req.employee)
    if not done:
        raise HTTPException(status_code=400, detail="Failed to create employee")
    return {"message": "Employee created successfully", "status": done}