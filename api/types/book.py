from pydantic import BaseModel

class Book(BaseModel):
    titulo: str
    editora: str
    isbn: int
    ano_publicacao: int
    autor: str
    id_loan: int
    id_categoria: int