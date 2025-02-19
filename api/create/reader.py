from fastapi import APIRouter, HTTPException
from api.types.reader import Reader
from database.services import reader as ReaderService
from database.utils import get_db
from pydantic import BaseModel

router = APIRouter()

class Req(BaseModel):
    reader: Reader

@router.post("/create/reader/")
def create_reader(req: Req):
    conn = get_db()
    print(req)
    done = ReaderService.ReaderService(conn).create_reader(req.reader)
    if not done:
        raise HTTPException(status_code=400, detail="Failed to create reader")
    return {"message": "Reader created successfully", "status": done}