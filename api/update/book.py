from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/book/{id}")
def update_book(titulo: str, editora: str, isbn: int, ano_publicacao: int, autor: str, id_loan: int, id_categoria:int):
    conn = get_db()
    book = BookService.BookService(conn).update(titulo, editora, isbn, ano_publicacao, autor, id_loan, id_categoria)
    if book is None:
        raise HTTPException(status_code=404, detail="Book não encontrado")
    return book