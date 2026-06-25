import sqlite3

    
def criar_banco():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    cursor.execute("""
CREATE TABLE Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin BOOLEAN NOT NULL DEFAULT 0,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL,
    pontos INTEGER NOT NULL DEFAULT 100,
    ranking INTEGER NOT NULL,
    status TEXT NOT NULL,
    data_cadastro DATE NOT NULL,
    UNIQUE (email, cpf, login)
);
""")

    cursor.execute("""
CREATE TABLE Aposta (
    idUsuario INTEGER,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idJogo INTEGER,
    data_aposta DATETIME NOT NULL,
    valor_aposta INTEGER NOT NULL,
    status TEXT NOT NULL,
    multiplicar_aposta REAL NOT NULL
);
""")

    cursor.execute("""
CREATE TABLE Jogo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAposta INTEGER,
    time_casa TEXT NOT NULL,
    time_fora TEXT NOT NULL,
    resultado INTEGER NOT NULL,
    odd REAL NOT NULL
);
""")

    cursor.execute("""
ALTER TABLE Aposta
ADD FOREIGN KEY (idUsuario) REFERENCES Usuario(id);
""")

    cursor.execute("""
ALTER TABLE Aposta
ADD FOREIGN KEY (idJogo) REFERENCES Jogo(id);
""")

    cursor.execute("""
ALTER TABLE Jogo
ADD FOREIGN KEY (idAposta) REFERENCES Aposta(id);
""")

    conexao.commit()
    conexao.close()