from api.types.reader import Reader
from database.services.generic import GenericService

class StudentService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "student")

class TeacherService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "teacher")

class ReaderService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "reader")
        self.StudentService = StudentService(conn)
        self.TeacherService = TeacherService(conn)
        
    def create_reader(self, reader:Reader):
        data = (reader.name, reader.address, reader.registration_date, reader.type)
        
        id = self.create(data)
        
        if reader.type == 'student':
            self.StudentService.create((id, reader.student_attributes.age, reader.student_attributes.school))
        else:
            self.TeacherService.create((id, reader.teacher_attributes.email, reader.teacher_attributes.subject))
        
        return True