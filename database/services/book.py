from database.services.generic import GenericService
from database.models.Book import Book

class BookService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "book", Book)  # Chama o construtor da classe pai (GenericService) com o nome da entidade