from pydantic import BaseModel, EmailStr, field_validator
from datetime import date
from services.validar_senha import validar_senha
from services.validar_idade import validar_idade

class UsuarioSchema(BaseModel):
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