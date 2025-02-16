from fastapi import APIRouter, HTTPException
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/loan/{id}")
def get_loan(id: int):
    print(id)
    conn = get_db()
    loan = LoanService.LoanService(conn).get(id)
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan não encontrado")
    return loan