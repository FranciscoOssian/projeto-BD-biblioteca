from fastapi import APIRouter, HTTPException
from database.services import intern as InternService
from database.utils import get_db

router = APIRouter()
    
@router.get("/create/intern/{id}")
def create_intern(fim_estagio:str):
    conn = get_db()
    intern = InternService.InternService(conn).create(fim_estagio)
    if intern is None:
        raise HTTPException(status_code=404, detail="Intern não encontrado")
    return intern