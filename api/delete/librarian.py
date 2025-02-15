from fastapi import APIRouter, HTTPException
from database.services import librarian as LibrarianService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/librarian/{id}")
def delete_librarian(id:int):
    conn = get_db()
    deleted = LibrarianService.LibrarianService(conn).delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Librarian não encontrado")
    return {"message": "Book deleted successfully"}