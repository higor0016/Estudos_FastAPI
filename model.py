from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel

class Genero(str, Enum):
    masculino = "Masculino"
    feminino = "Feminino"

class Funcao(str, Enum):
    admin = "admin"
    usuario = "usuario"

class Usuario(BaseModel):
    id: Optional[UUID] = uuid4()
    primeiro_nome: str
    sobrenome: str
    genero: Genero
    funcoes: List[Funcao]

class Atualiza_Usuario(BaseModel):
    primeiro_nome: Optional[str]
    sobrenome: Optional[str]
    funcoes: Optional[List[Funcao]]