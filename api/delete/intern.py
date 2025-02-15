from fastapi import APIRouter, HTTPException
from database.services import intern as InternService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/intern/{id}")
def delete_intern(id:int):
    conn = get_db()
    deleted = InternService.InternService(conn).delete(id)
    if deleted:
        raise HTTPException(status_code=404, detail="Intern não encontrado")
    return {"message": "intern deleted successfully"}