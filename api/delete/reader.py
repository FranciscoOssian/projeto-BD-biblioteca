from fastapi import APIRouter, HTTPException
from database.services import reader as ReaderService
from database.utils import get_db

router = APIRouter()
    
@router.delete("/delete/reader/{id}")
def delete_reader(id:int):
    conn = get_db()
    deleted = ReaderService.ReaderService(conn).delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Reader não encontrado")
    return {"message": "Book deleted successfully"}