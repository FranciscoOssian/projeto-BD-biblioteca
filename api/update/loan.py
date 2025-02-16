import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()

class Req(BaseModel):
    id: int

@router.put("/return/book")
def update_loan(req: Req):
    conn = get_db()
    loan = LoanService.LoanService(conn).get(req.id)
    updated = LoanService.LoanService(conn).update(
        (datetime.now(), loan.data_devolucao, loan.id_livro, loan.id_leitor)
    )
    if updated is None:
        raise HTTPException(status_code=400, detail="Loan não atualizado")
    return {"message": "Book updated successfully", "book": updated}