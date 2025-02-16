from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    titulo: str
    editora: str
    isbn: str
    ano_publicacao: int
    autor: str
    id_loan: Optional[int] = None