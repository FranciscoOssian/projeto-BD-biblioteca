from fastapi import APIRouter, HTTPException
from database.services import reader as ReaderService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/reader/{id}")
def update_reader(id:int, nome:str, endereco:str, data_registro:str, tipo_leitor:str):
    conn = get_db()
    updated = ReaderService.ReaderService(conn).update(id, nome, endereco, data_registro, tipo_leitor)
    if updated is None:
        raise HTTPException(status_code=400, detail="Reader não atualizado")
    return updated