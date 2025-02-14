from database.services.generic import GenericService

class ReaderService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "reader")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        
    