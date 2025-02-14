from database.services.generic import GenericService

class BookService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "book")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        
    