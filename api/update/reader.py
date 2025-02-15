from fastapi import APIRouter, HTTPException
from database.services import reader as ReaderService
from database.utils import get_db

router = APIRouter()
    
@router.get("/update/reader/{id}")
def update_reader(nome:str, endereco:str, data_registro:str, tipo_leitor:str):
    conn = get_db()
    reader = ReaderService.ReaderService(conn).update(nome, endereco, data_registro, tipo_leitor)
    if reader is None:
        raise HTTPException(status_code=404, detail="Reader não encontrado")
    return reader