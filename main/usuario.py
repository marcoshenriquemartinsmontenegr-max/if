from pydantic import BaseModel, EmailStr, field_validator
from datetime import date
from .validar_senha import validar_senha
from .validar_idade import validar_idade
from database.banco_dados import inserir_usuario 

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
    data_cadastro: date

    @field_validator("senha")
    @classmethod
    def validar_campo_senha(cls, senha):
        return validar_senha(senha)

    @field_validator("data_nascimento")
    @classmethod
    def validar_campo_idade(cls, data_nascimento):
        return validar_idade(data_nascimento)   


usuario = Usuario(
    nome="Marcos",
    email="marcos@gmail.com",
    cpf="06712345678",
    data_nascimento="2005-12-13",
    login="mhmm",
    senha="12345Hm@",
    data_cadastro="2022-11-16"
)

inserir_usuario
print("Usuario salvo")

print(usuario)