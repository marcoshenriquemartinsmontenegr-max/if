from services.usuario_services import buscar_usuario
from main.aposta import Aposta
from datetime import date
from database.banco_dados import inserir_aposta


def registrar_aposta(aposta: Aposta, login):
    usuario = buscar_usuario(login)
    data_aposta = date.now()
    id_usuario = usuario[0]
    pontos = usuario[8]
    if pontos < aposta.valor_aposta:
        raise ValueError("Pontos insuficientes")
    return usuario

inserir_aposta(aposta, id_usuario, data_aposta)