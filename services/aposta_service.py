from datetime import date
from database.banco_dados import Session, atualizar_pontos, inserir_aposta
from models.aposta import Aposta as ApostaDB  # Model do Banco
from models.aposta import ApostaSchema  # Schema do Pydantic
from models.usuario import Usuario  # Model do Banco
from services.usuario_service import buscar_usuario


def registrar_aposta(aposta: ApostaSchema, login: str):
    usuario = buscar_usuario(login)
    if not usuario:
        raise ValueError("Usuário não encontrado")
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
    with Session() as db:
        aposta = db.query(ApostaDB).filter(ApostaDB.id == id_aposta).first()
        if aposta:
            return aposta.status
        return "Aposta não encontrada"




def multiplicar_aposta(id_aposta: int, id_usuario: int, multiplicador: int):
    with Session() as db:
        aposta = db.query(ApostaDB).filter(ApostaDB.id == id_aposta).first()
        if not aposta:
            return {"erro": "Aposta não encontrada."}
        usuario = db.query(Usuario).filter(Usuario.id == id_usuario).first()
        if not usuario:
            return {"erro": "Usuário não encontrado."}
        novo_valor = aposta.valor_aposta * multiplicador
        custo_adicional = novo_valor - aposta.valor_aposta
        if usuario.pontos < custo_adicional:
            return {"erro": "Pontos insuficientes."}
        usuario.pontos -= custo_adicional
        aposta.valor_aposta = novo_valor
        db.commit()
        return {
            "sucesso": True,
            "novo_valor_aposta": aposta.valor_aposta,
            "saldo_restante": usuario.pontos,
        }