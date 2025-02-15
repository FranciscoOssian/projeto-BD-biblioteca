from fastapi import APIRouter, HTTPException
from database.services import intern as InternService
from database.utils import get_db

router = APIRouter()
    
@router.put("/update/intern/{id}")
def update_intern(id:int, fim_estagio:str):
    conn = get_db()
    updated = InternService.InternService(conn).update(id, fim_estagio)
    if updated is None:
        raise HTTPException(status_code=400, detail="Intern não atualizado")
    return {"message": "Book updated successfully", "book": updated}