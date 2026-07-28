from datetime import date
from database.banco_dados import Aposta as ApostaDB
from database.banco_dados import atualizar_pontos, inserir_aposta
from main.aposta import Aposta as ApostaSchema
from services.usuario_service import buscar_usuario
from database.banco_dados import Session
from main.aposta import Aposta

def registrar_aposta(aposta: ApostaSchema, login: str):
    usuario = buscar_usuario(login)
    if usuario.pontos < aposta.valor_aposta:
        raise ValueError('Pontos insuficientes')
    
    aposta_banco = ApostaDB(
        idUsuario=usuario.id,
        idJogo=aposta.id_jogo,
        data_aposta=date.today(),
        valor_aposta=aposta.valor_aposta,
        multiplicar_aposta=aposta.multiplicar_aposta,
        status=aposta.status
    )
    inserir_aposta(aposta_banco)
    novos_pontos = usuario.pontos - aposta.valor_aposta
    atualizar_pontos(usuario.id, novos_pontos)
    return aposta_banco




def consultar_status_aposta(id_aposta: int):
    db = Session()
    aposta = db.query(Aposta).filter(Aposta.id == id_aposta).first()
    db.close()
    if aposta:
        return aposta.status
    return "Aposta não encontrada"



    
