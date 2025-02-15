from fastapi import APIRouter, HTTPException
from database.services import loan as LoanService
from database.utils import get_db
from pydantic import BaseModel, Field

router = APIRouter()
    
class LoanCreateRequest(BaseModel):
    data_retirado:str = Field(..., example=""), 
    data_devolucao:str = Field(..., example=""), 
    id_livro:int = Field(..., example=""), 
    id_leitor:int = Field(..., example="")
    
@router.post("/create/loan/", response_class=dict)
def create_loan(loan_data: LoanCreateRequest):
    conn = get_db()
    loan = LoanService.LoanService(conn).create(
        data_retirado = loan_data.data_retirado,
        data_devolucao = loan_data.data_devolucao,
        id_livro = loan_data.id_livro,
        id_leitor = loan_data.id_leitor
    )
    if loan is None:
        raise HTTPException(status_code=400, detail="Failed to create loan")
    return {"message": "loan created successfully", "loan": loan}