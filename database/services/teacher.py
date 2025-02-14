from database.services.generic import GenericService

class TeacherService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "teacher")
        
    