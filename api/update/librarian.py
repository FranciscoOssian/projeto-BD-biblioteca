from fastapi import APIRouter, HTTPException
from database.services import librarian as LibrarianService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/librarian/{id}")
def update_librarian(id: int, tempo_trabalhado:str):
    conn = get_db()
    updated = LibrarianService.LibrarianService(conn).update(id, tempo_trabalhado)
    if updated is None:
        raise HTTPException(status_code=400, detail="Librarian não atualizado")
    return {"message": "Book updated successfully", "book": updated}