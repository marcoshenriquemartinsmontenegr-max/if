import sqlite3

def validar_idade(data_nascimento):
    if data_nascimento >= 18:
        print("Menor de idade")
    
def validar_senha(senha):
    if len(senha) < 8:
        print("minímo 8 caracteres!")
        return False
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        if  letra.islower():
            tem_maiuscula = True
        if  letra.isdigit():
            tem_numero = True
        if not letra.isalpha() and not letra.isdigit():
            tem_especial = True
    

class Usuario:
    def __init__(self, nome, email, cpf, data_nascimento, login, senha):
        self.pontos = 100
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.login = login
        self.senha = senha

    def criar_usuario(self):
        conexao = sqlite3.connect("usuarios.db")
        cursor = conexao.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    pontos INT,
    nome TEXT,
    email TEXT,
    cpf TEXT,
    data_nascimento DATE,
    login TEXT,
    senha TEXT
)
""")
        

        cursor.execute("""
        INSERT INTO usuarios (pontos ,nome, email, cpf, data_nascimento, login, senha)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            self.pontos,
            self.nome,
            self.email,
            self.cpf,
            self.data_nascimento,
            self.login,
            self.senha
        ))

        conexao.commit()
        conexao.close()