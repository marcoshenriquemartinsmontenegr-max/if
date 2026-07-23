from services.usuario_service import buscar_usuario
from main.aposta import Aposta
from datetime import date
from database.banco_dados import inserir_aposta
from database.banco_dados import atualizar_pontos


def registrar_aposta(aposta: Aposta, login):
    usuario = buscar_usuario(login)
    data_aposta = date.today()
    id_usuario = usuario[0]
    pontos = usuario[8]
    if pontos < aposta.valor_aposta:
        raise ValueError("Pontos insuficientes")
    novos_pontos = pontos - aposta.valor_aposta 
    inserir_aposta(aposta, id_usuario, data_aposta)
    atualizar_pontos(id_usuario, novos_pontos)