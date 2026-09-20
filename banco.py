import sqlite3

def conectar():
    conexao = sqlite3.connect("financeiro.db")
    return conexao

def inserir_lancamento(descricao, valor, tipo, data, categoria):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO lancamentos (descricao, valor, tipo, data, categoria) VALUES (?,?,?,?,?)",(descricao,valor,tipo,data,categoria))

    conexao.commit()
    conexao.close()

def buscar_lancamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM lancamentos")

    lancamentos = cursor.fetchall()
    conexao.close()
    return lancamentos

def excluir_lancamento(id_lancamento):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE * FROM lancamentos WHERE id = ?",(id_lancamento))

    conexao.commit()
    conexao.close()


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