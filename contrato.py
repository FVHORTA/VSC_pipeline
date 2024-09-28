from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr

from pydantic import BaseModel


class Delivery(BaseModel):
    nome: EmailStr   # pip install email-validator
    idade: int
    data: datetime
    status: str
    hora: datetime
    data_hora: str


