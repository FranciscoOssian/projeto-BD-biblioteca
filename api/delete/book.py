from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/book/{id}")
def delete_book(id:int):
    conn = get_db()
    deleted = BookService.BookService(conn).delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book não encontrado")
    return {"message": "Book deleted successfully"}