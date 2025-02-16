from typing import Literal, Optional
from pydantic import BaseModel

class Student(BaseModel):
    age: int
    school: str

class Teacher(BaseModel):
    email: str
    subject: str

class Reader(BaseModel):
    name: str
    address: str
    registration_date: str 
    type: Literal['student', 'teacher']
    student_attributes: Optional[Student] = None
    teacher_attributes: Optional[Teacher] = None