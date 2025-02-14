from database.services.generic import GenericService

class LibrarianService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "librarian")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        
    