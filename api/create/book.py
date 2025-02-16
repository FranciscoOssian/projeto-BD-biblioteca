from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db
from pydantic import BaseModel

router = APIRouter()

class BookCreateRequest(BaseModel):
    titulo: str
    editora: str
    isbn: int
    ano_publicacao: int
    autor: str
    id_loan: int
    id_categoria: int


@router.post("/create/book/", response_class=dict)
def create_book(book_data: BookCreateRequest):
    conn = get_db()
    book = BookService.BookService(conn).create(
        titulo=book_data.titulo,
        editora=book_data.editora, 
        isbn=book_data.isbn, 
        ano_publicacao=book_data.ano_publicacao, 
        autor=book_data.autor, 
        id_loan=book_data.id_loan, 
        id_categoria=book_data.id_categoria
    )
    if book is None:
        raise HTTPException(status_code=400, detail="Failed to create book")
    return {"message": "Book created successfully", "book": book}