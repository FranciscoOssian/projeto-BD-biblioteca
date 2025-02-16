from fastapi import APIRouter, HTTPException
from database.services import loan as LoanService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/loan/{id}")
def update_loan(id:int, data_retirado:str, data_devolucao:str, id_livro:int, id_leitor:int):
    conn = get_db()
    updated = LoanService.LoanService(conn).update(id, data_retirado, data_devolucao, id_livro, id_leitor)
    if updated is None:
        raise HTTPException(status_code=400, detail="Loan não atualizado")
    return {"message": "Book updated successfully", "book": updated}