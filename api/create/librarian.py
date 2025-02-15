from fastapi import APIRouter, HTTPException
from database.services import librarian as LibrarianService
from database.utils import get_db
from pydantic import BaseModel, Field


router = APIRouter()

class LibrarianCreateRequest(BaseModel):
    tempo_trabalhado : str = Field(..., example="12:00:00")


@router.post("/create/librarian/", response_class=dict)
def create_librarian(librarian_data: LibrarianCreateRequest):
    conn = get_db()
    librarian = LibrarianService.LibrarianService(conn).create(
        tempo_trabalhado = librarian_data.tempo_trabalhado
    )
    if librarian is None:
        raise HTTPException(status_code=400, detail="Failed to create librarian")
    return {"message": "librarian created successfully", "librarian": librarian}