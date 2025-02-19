from fastapi import APIRouter, HTTPException
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/loan/{id}")
def delete_loan(id:int):
    conn = get_db()
    deleted = LoanService.LoanService(conn).delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Loan não encontrado")
    return {"message": "Book deleted successfully"}