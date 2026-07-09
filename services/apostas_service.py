from usuario_services import buscar_usuario
from main.aposta import Aposta


def registrar_aposta(aposta: Aposta, login):
    usuario = buscar_usuario(login)
    pontos = usuario[8]
    if pontos < aposta.valor_aposta:
        raise ValueError("Pontos insuficientes")
    return usuario

