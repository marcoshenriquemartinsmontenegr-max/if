from database.banco_dados import buscar_usuario_por_login



def buscar_usuario(login):
    usuario = buscar_usuario_por_login(login)
    if usuario is None:
        raise ValueError("Usuário não encontrado")

    return usuario