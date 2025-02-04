from database.services.generic import GenericService

class DataBaseService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "database") 
        
    