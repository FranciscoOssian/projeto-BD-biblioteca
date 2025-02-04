from database.services.generic import GenericService

class StudentService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "student")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        
    