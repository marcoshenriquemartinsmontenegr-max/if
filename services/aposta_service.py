from datetime import date
from database.banco_dados import atualizar_pontos, inserir_aposta
from main.aposta import Aposta
from services.usuario_service import buscar_usuario


def registrar_aposta(aposta: Aposta, login):
    usuario = buscar_usuario(login)
    if usuario.pontos < aposta.valor_aposta:
        raise ValueError('Pontos insuficientes')
    novos_pontos = usuario.pontos - aposta.valor_aposta
    aposta.idUsuario = usuario.id
    aposta.data_aposta = date.today()
    inserir_aposta(aposta)
    atualizar_pontos(usuario.id, novos_pontos)