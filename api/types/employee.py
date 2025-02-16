from datetime import time
from typing import Literal
from pydantic import BaseModel

class Intern(BaseModel):
    fim_estagio: time

class Librarian(BaseModel):
    tempo_trabalhado: int

class Employee(BaseModel):
    nome: str
    telefone: str
    role: Literal['intern', 'librarian']
    intern_attributes: Intern
    librarian_attributes: Librarian