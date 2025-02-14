from database.services.generic import GenericService

class LoanService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "loan")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        
    