from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/book/{id}")
def get_book(id: int):
    print(id)
    conn = get_db()
    book = BookService.BookService(conn).get(id)
    if book is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book