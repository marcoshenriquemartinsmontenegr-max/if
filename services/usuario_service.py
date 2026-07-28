from database.banco_dados import Usuario as UsuarioDB
from database.banco_dados import buscar_usuario_por_login, inserir_usuario
from main.usuario import UsuarioSchema


def cadastrar_usuario(dados_usuario: UsuarioSchema):
    usuario_existente = buscar_usuario_por_login(dados_usuario.login)
    if usuario_existente:
        raise ValueError('Já existe um usuário cadastrado com esse login!')
    usuario_banco = UsuarioDB(**dados_usuario.model_dump())
    inserir_usuario(usuario_banco)
    return usuario_banco


def buscar_usuario(login: str):
    usuario = buscar_usuario_por_login(login)
    if usuario is None:
        raise ValueError('Usuário não encontrado')
    return usuario