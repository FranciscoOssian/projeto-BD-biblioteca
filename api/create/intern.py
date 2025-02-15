from fastapi import APIRouter, HTTPException
from database.services import intern as InternService
from database.utils import get_db
from pydantic import BaseModel, Field


router = APIRouter()

class InternCreateRequest(BaseModel):
    fim_estagio: str = Field(..., example="The Great Gatsby")

@router.post("/create/Intern/", response_class=dict)
def create_intern(intern_data: InternCreateRequest):
    conn = get_db()
    intern = InternService.InternService(conn).create(
        fim_estagio = intern_data.fim_estagio
    )
    if intern is None:
        raise HTTPException(status_code=400, detail="Failed to create intern")
    return {"message": "Book created successfully", "intern": intern}