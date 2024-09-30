from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveInt, Enum

from pydantic import BaseModel

class statusAI(str, Enum):
    ativo = 'Ativo'
    inativo = 'Inativo'

class cadastros(BaseModel):
    nome: EmailStr   # pip install email-validator
    idade: PositiveInt
    data_nascimento: datetime
    status: str
    dttime: datetime


