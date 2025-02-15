from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/book/{id}")
def delete_book(id:int):
    conn = get_db()
    book = BookService.BookService(conn).delete(id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book não encontrado")
    return book