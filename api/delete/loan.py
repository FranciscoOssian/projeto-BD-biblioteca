from fastapi import APIRouter, HTTPException
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()
    
@router.get("/delete/loan/{id}")
def delete_loan(id:int):
    conn = get_db()
    loan = LoanService.LoanService(conn).delete(id)
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan não encontrado")
    return loan