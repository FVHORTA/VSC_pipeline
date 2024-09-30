from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveInt

from pydantic import BaseModel

class statusAI(str, Enum):
    ativo = 'Ativo'
    inativo = 'Inativo'

class cadastros(BaseModel):
    nome: str
    idade: PositiveInt
    data: datetime
    email: EmailStr   # pip install email-validator
    status: statusAI
    data_hora: datetime
   


