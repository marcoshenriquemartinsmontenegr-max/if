from pydantic import BaseModel




class Aposta(BaseModel):
    id_jogo: int
    valor_aposta: int
    status: str = "em aberto"
    multiplicar_aposta: float
