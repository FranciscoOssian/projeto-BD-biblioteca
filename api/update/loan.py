from fastapi import APIRouter, HTTPException
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/loan/{id}")
def update_loan(data_retirado:str, data_devolucao:str, id_livro:int, id_leitor:int):
    conn = get_db()
    loan = LoanService.LoanService(conn).update(data_retirado, data_devolucao, id_livro, id_leitor)
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan não encontrado")
    return loan