from fastapi import APIRouter, HTTPException
from database.services import reader as ReaderService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/reader/{id}")
def get_reader(id: int):
    print(id)
    conn = get_db()
    reader = ReaderService.ReaderService(conn).get(id)
    if reader is None:
        raise HTTPException(status_code=404, detail="Reader não encontrado")
    return reader

@router.get("/read/readers")
def get_book_all():
    conn = get_db()
    book = ReaderService.ReaderService(conn).get_all()
    if book is None:
        raise HTTPException(status_code=404, detail="Readers não encontrados")
    return book 