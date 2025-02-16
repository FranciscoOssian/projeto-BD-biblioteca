from typing import List
from fastapi import APIRouter, HTTPException
from database.services import book as BookService
from database.utils import get_db
from pydantic import BaseModel

router = APIRouter()

class Book(BaseModel):
    titulo: str
    editora: str
    isbn: int
    ano_publicacao: int
    autor: str
    id_loan: int
    id_categoria: int

class ReqBody(BaseModel):
    books: List[Book]

@router.post("/create/books/")
def create_book(req: ReqBody):
    conn = get_db()
    tuplas = [
        (book.titulo, book.editora, book.isbn,
         book.ano_publicacao, book.autor,
         book.id_loan, book.id_categoria)
        for book in req.books
    ]
    status = BookService.BookService(conn).create_many(tuplas)
    if status is None or status is False:
        raise HTTPException(status_code=500, detail="Failed to create books")
    return {"message": "Book created successfully", "staatus": status}