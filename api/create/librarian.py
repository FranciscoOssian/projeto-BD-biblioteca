from fastapi import APIRouter, HTTPException
from database.services import librarian as LibrarianService
from database.utils import get_db

router = APIRouter()
    
@router.post("/create/librarian/{id}")
def create_librarian(tempo_trabalhado:str):
    conn = get_db()
    librarian = LibrarianService.LibrarianService(conn).create(tempo_trabalhado)
    if librarian is None:
        raise HTTPException(status_code=404, detail="Librarian não encontrado")
    return librarian