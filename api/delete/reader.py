from fastapi import APIRouter, HTTPException
from database.services import reader as ReaderService
from database.utils import get_db

router = APIRouter()
    
@router.get("/delete/reader/{id}")
def delete_reader(id:int):
    conn = get_db()
    reader = ReaderService.ReaderService(conn).delete(id)
    if reader is None:
        raise HTTPException(status_code=404, detail="Reader não encontrado")
    return reader