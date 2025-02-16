from fastapi import APIRouter, HTTPException
from database.services import reader as ReaderService
from database.utils import get_db
from pydantic import BaseModel


router = APIRouter()
    
class ReaderCreateRequest(BaseModel):
    nome: str
    endereco: str
    data_registro:str
    tipo_leitor:str

@router.post("/create/reader/", response_class=dict)
def create_reader(reader_data: ReaderCreateRequest):
    conn = get_db()
    reader = ReaderService.ReaderService(conn).create(
        nome = reader_data.nome,
        endereco = reader_data.endereco,
        data_registro = reader_data.data_registro,
        tipo_leitor = reader_data.tipo_leitor
    )
    if reader is None:
        raise HTTPException(status_code=400, detail="Failed to create reader")
    return  {"message": "Reader created successfully", "reader": reader}