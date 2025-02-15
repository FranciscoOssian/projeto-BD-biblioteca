from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db
from pydantic import BaseModel, Field

router = APIRouter()

class BookCreateRequest(BaseModel):
    titulo: str = Field(..., example="The Great Gatsby")
    editora: str = Field(..., example="Scribner")
    isbn: int = Field(..., example=9780743273565)
    ano_publicacao: int = Field(..., example=1925)
    autor: str = Field(..., example="F. Scott Fitzgerald")
    id_loan: int = Field(..., example=1)
    id_categoria: int = Field(..., example=2)


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