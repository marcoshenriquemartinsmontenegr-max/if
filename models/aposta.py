from pydantic import BaseModel

class ApostaSchema(BaseModel):
    id_jogo: int
    valor_aposta: int
    status: str = "em aberto"
    multiplicar_aposta: float