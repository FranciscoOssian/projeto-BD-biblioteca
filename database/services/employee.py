from database.services.generic import GenericService

class EmployeeService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "employee")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        
    