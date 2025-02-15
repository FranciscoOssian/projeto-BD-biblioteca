from fastapi import APIRouter, HTTPException
from database.services import intern as InternService
from database.utils import get_db

router = APIRouter()
    
@router.get("/read/intern/{id}")
def get_intern(id: int):
    conn = get_db()
    intern = InternService.InternService(conn).get(id)
    if intern is None:
        raise HTTPException(status_code=404, detail="Estagiário não encontrado")
    return intern