from typing import Optional
from pydantic import BaseModel

class Loan(BaseModel):
    data_retirado: Optional[str] = None
    data_devolucao: str
    id_leitor: int
    id_livro: int