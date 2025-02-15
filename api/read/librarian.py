from fastapi import APIRouter, HTTPException
from database.services import librarian as LibrarianService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/librarian/{id}")
def get_librarian(id: int):
    print(id)
    conn = get_db()
    librarian = LibrarianService.LibrarianService(conn).get(id)
    if librarian is None:
        raise HTTPException(status_code=404, detail="Librarian não encontrado")
    return librarian