from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/book/{id}")
def update_book(id:int, titulo: str, editora: str, isbn: int, ano_publicacao: int, autor: str, id_loan: int, id_categoria:int):
    conn = get_db()
    updated = BookService.BookService(conn).update(id, titulo, editora, isbn, ano_publicacao, autor, id_loan, id_categoria)
    if updated is None:
        raise HTTPException(status_code=400, detail="Book não atualizado")
    return {"message": "Book updated successfully", "book": updated}