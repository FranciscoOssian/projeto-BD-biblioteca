from api.types.employee import Employee
from database.services.generic import GenericService

class InternServices(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "intern")

class LibrarianServices(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "librarian")

class EmployeeService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "employee")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        self.InterServices = InternServices(conn)
        self.LibrarianServies = LibrarianServices(conn)
        
    def create_employee(self, employee:Employee):
        data = (employee.nome, employee.telefone)
        
        id = self.create(data)
        
        if employee.role == 'inter':
            self.InterServices.create((id, employee.intern_attributes.fim_estagio))
        else:
            self.LibrarianServies.create((id, employee.librarian_attributes.tempo_trabalhado))
        
        return True