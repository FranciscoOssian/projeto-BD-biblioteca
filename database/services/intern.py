from database.services.generic import GenericService
from database.models import Intern

class InternService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "intern")  # Chama o construtor da classe pai (GenericService) com o nome da entidade
        
    