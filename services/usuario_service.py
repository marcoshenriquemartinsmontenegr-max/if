from sqlalchemy import select
from database.banco_dados import Session
from database.banco_dados import Usuario as UsuarioDB  # Model do Banco
from database.banco_dados import Aposta as ApostaDB # Model do Banco
from models.usuario import UsuarioSchema  # Schema do Pydantic
from database.banco_dados import Jogo as JogoDB


def cadastrar_usuario(dados_usuario: UsuarioSchema):
    usuario_existente = buscar_usuario_por_login(dados_usuario.login)
    if usuario_existente:
        raise ValueError("Já existe um usuário cadastrado com esse login!")

    usuario_banco = UsuarioDB(**dados_usuario.model_dump())
    inserir_usuario(usuario_banco)
    return usuario_banco


def buscar_usuario(login: str):
    usuario = buscar_usuario_por_login(login)
    if usuario is None:
        raise ValueError("Usuário não encontrado")
    return usuario


def inserir_usuario(usuario: UsuarioDB):
    with Session() as session:
        session.add(usuario)
        session.commit()


def buscar_usuario_por_login(login: str):
    with Session() as session:
        stmt = select(UsuarioDB).where(UsuarioDB.login == login)
        return session.scalars(stmt).first()


def deslogar(id_usuario: int):
    with Session() as session:
        usuario = session.query(UsuarioDB).filter(UsuarioDB.id == id_usuario).first()
        if not usuario:
            return {"erro": "Usuário não encontrado"}
        usuario.status = False
        session.commit()
        return {"sucesso": True, "mensagem": "Usuário inativado com sucesso."}


def alterar_senha(id_usuario: int, senha_atual: str, nova_senha: str):
    if len(nova_senha) < 8:
        return {"erro": "A nova senha deve ter no mínimo 8 caracteres."}
    with Session() as session:
        usuario = session.query(UsuarioDB).filter(UsuarioDB.id == id_usuario).first()
        if not usuario:
            return {"erro": "Usuário não encontrado."}
        if usuario.senha != senha_atual:
            return {"erro": "A senha atual está incorreta."}
        usuario.senha = nova_senha
        session.commit()
        return {"sucesso": True, "mensagem": "Senha alterada com sucesso."}



def consultar_saldo_pontos(usuario_id: int):
    with Session() as session:
        stmt = select(UsuarioDB).where(UsuarioDB.id == usuario_id)
        usuario = session.scalars(stmt).first()
        if not usuario:
            return "Usuário não encontrado."
        if usuario.status == "inativo" or usuario.status == "zerado":
            return f"Saldo: {usuario.pontos} pts. Sua conta está {usuario.status} e você não pode mais realizar apostas."
        return f"Seu saldo atual é de {usuario.pontos} pontos."



def ranking():
    with Session() as session:
        stmt = select(UsuarioDB).order_by(UsuarioDB.acertos.desc(), UsuarioDB.pontos.desc())
        jogadores = session.scalars(stmt).all()
        return jogadores




def listar_todos_usuarios():
    with Session() as session:
        stmt = select(UsuarioDB)
        usuarios = session.scalars(stmt).all()
        return usuarios



def buscar_usuario_por_cpf(cpf: str):
    with Session() as session:
        stmt = select(UsuarioDB).where(UsuarioDB.cpf == cpf)
        usuario = session.scalars(stmt).first()
        return usuario



def listar_todas_partidas():
    with Session() as session:
        stmt = select(JogoDB)
        return session.scalars(stmt).all()



def buscar_apostas_por_partida(jogo_id: int):
    with Session() as session:
        stmt = select(ApostaDB).where(ApostaDB.jogo_id == jogo_id)
        apostas = session.scalars(stmt).all()
        return apostas