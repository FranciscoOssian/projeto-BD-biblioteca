from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.types.loan import Loan
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()

class Req(BaseModel):
    loan: Loan
    
@router.post("/create/loan/")
def create_loan(req: Req):
    conn = get_db()
    print(req)
    tupla = (req.loan.data_retirado, req.loan.data_devolucao,
         req.loan.id_leitor, req.loan.id_livro)
    id = LoanService.LoanService(conn).create(tupla)
    if id is None:
        raise HTTPException(status_code=400, detail="Failed to create loan")
    return {"message": "loan created successfully", "loan": id}