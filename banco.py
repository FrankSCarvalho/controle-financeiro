import sqlite3

def conectar():
    conexao = sqlite3.connect("financeiro.db")
    return conexao


conexao = conectar()
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS lancamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        tipo TEXT NOT NULL,
        data TEXT NOT NULL,
        categoria TEXT NOT NULL
    )
""")

conexao.commit()

conexao.close()