#Eu pedi pra IA testar pra mim
from datetime import date
from main.aposta import Aposta as ApostaSchema
from main.usuario import UsuarioSchema
from services.aposta_service import registrar_aposta
from services.usuario_service import buscar_usuario, cadastrar_usuario

print("--- 🧪 INICIANDO TESTES DO SISTEMA ---")

# 1. TESTE DE CADASTRO DE USUÁRIO
print("\n1. Criando um novo usuário com Pydantic...")
novo_usuario = UsuarioSchema(
    nome="Marcos Montenegro",
    email="marcos@email.com",
    cpf="12345678900",
    data_nascimento="2005-12-13",
    login="marcos_test",
    senha="12345Hm@",
    data_cadastro=date.today(),
)

try:
    cadastrar_usuario(novo_usuario)
    print("✅ Usuário cadastrado com sucesso no SQLite via SQLAlchemy!")
except Exception as e:
    print(f"⚠️ Aviso ao cadastrar usuário: {e}")

# 2. TESTE DE BUSCA DE USUÁRIO
print("\n2. Buscando usuário cadastrado...")
usuario_banco = buscar_usuario("marcos_test")
print(
    f"👤 Usuário encontrado: {usuario_banco.nome} | ID: {usuario_banco.id} | Pontos Iniciais: {usuario_banco.pontos}"
)

# 3. TESTE DE CRIAÇÃO E REGISTRO DE APOSTA
print("\n3. Criando e registrando uma aposta...")
nova_aposta = ApostaSchema(
    id_jogo=1, valor_aposta=20, status="em aberto", multiplicar_aposta=1.85
)

try:
    aposta_registrada = registrar_aposta(nova_aposta, login="marcos_test")
    print("✅ Aposta realizada com sucesso!")

    # 4. CONFERINDO SALDO DE PONTOS ATUALIZADO
    usuario_atualizado = buscar_usuario("marcos_test")
    print(
        f"💰 Pontos restantes do usuário: {usuario_atualizado.pontos} (esperado: 80)"
    )

except Exception as e:
    print(f"❌ Erro ao realizar aposta: {e}")

print("\n--- 🏁 TESTE FINALIZADO ---")

