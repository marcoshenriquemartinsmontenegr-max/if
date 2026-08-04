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



def deslogar(id_usuario: int):
# 1. Conectar com o banco de dados (Sessionlocal)

# 2. Buscar o usuário pelo id

# 3. Mudar o campo de status para inativo (False)

# 4. Salvar no banco (db.commit())

# 5. Fechar conexão (db.close())
    pass



def alterar_senha(id_usuario, senha_atual, nova_senha):
    # 1. Conectar com o banco de dados (SessionLocal)
    
    # 2. Buscar o usuário pelo id no banco
    
    # 3. Validar se o usuário foi encontrado
    
    # 4. Validar se a 'senha_atual' recebida confere com a senha salva no banco
    
    # 5. (Opcional) Validar se a 'nova_senha' atende aos requisitos (ex: tamanho mínimo)
    
    # 6. Atualizar o campo do banco com a 'nova_senha' recebida
    
    # 7. Salvar as alterações no banco (db.commit())
    
    # 8. Fechar a conexão com o banco (db.close())
    
    # 9. Retornar mensagem de sucesso
    pass  



