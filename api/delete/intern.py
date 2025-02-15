from fastapi import APIRouter, HTTPException
from database.services import intern as InternService
from database.utils import get_db

router = APIRouter()
    
@router.get("/delete/intern/{id}")
def delete_intern(id:int):
    conn = get_db()
    intern = InternService.InternService(conn).delete(id)
    if intern is None:
        raise HTTPException(status_code=404, detail="Intern não encontrado")
    return intern