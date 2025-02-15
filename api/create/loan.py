from fastapi import APIRouter, HTTPException
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()
    
@router.get("/create/loan/{id}")
def create_loan(data_retirado:str, data_devolucao:str, id_livro:int, id_leitor:int):
    conn = get_db()
    loan = LoanService.LoanService(conn).create(data_retirado, data_devolucao, id_livro, id_leitor)
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan não encontrado")
    return loan