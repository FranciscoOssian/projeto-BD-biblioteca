from typing import Literal, Optional
from pydantic import BaseModel

class Intern(BaseModel):
    fim_estagio: str

class Librarian(BaseModel):
    tempo_trabalhado: int

class Employee(BaseModel):
    nome: str
    telefone: str
    role: Literal['intern', 'librarian']
    intern_attributes: Optional[Intern] = None
    librarian_attributes: Optional[Librarian] = None