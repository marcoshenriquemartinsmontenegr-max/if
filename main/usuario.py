from pydantic import BaseModel, EmailStr, field_validator




class Usuario(BaseModel):
    nome: str
    email: str
    senha: str
    pontos: int = 100