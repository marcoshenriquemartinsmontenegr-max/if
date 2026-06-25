from pydantic import BaseModel, EmailStr, field_validator
from datetime import date
from validar_senha import validar_senha


class Usuario(BaseModel):
    nome: str 
    admin: bool = False
    email: EmailStr 
    cpf: str 
    data_nascimento: date 
    login: str 
    senha: str 
    pontos: int = 100
    ranking: int = 0
    status: str = "ativo"

usuario = Usuario(
    nome="Marcos",
    email="marcos@gmail.com",
    cpf="06712345678",
    data_nascimento="2005-12-13",
    login="mhmm",
    senha="Senha123#"
)

print(usuario)

@field_validator("senha")
@classmethod
def validar_campo_senha(cls, senha):
    validar_senha(senha)
    return senha