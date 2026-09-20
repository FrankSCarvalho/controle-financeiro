import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

from banco import inserir_lancamento

def pegar_descricao():
    descricao = entrada_descricao.get()    

    if descricao == "":
        print("A descrição está vazia")
        return None
    else:
        return descricao

def pegar_valor():
    valor = entrada_valor.get()
    if valor == "":
        print("O valor está vazio.")
        return None

    try:
        valor = float(valor)
        return valor
    except ValueError:
        print("O valor informado é inválido.")
        return None

def pegar_tipo():
    valor = tipo.get()

    if valor == "":
        print("Nenhum tipo foi selecionado.")
        return None

    return valor
def validar_data():
    valor = entrada_data.get()

    try:
        data = datetime.strptime(valor, "%d/%m/%Y")
        return data.strftime("%d/%m/%Y")
    except ValueError:
        print("A data informada é inválida.")
        return None

def cadastrar():
    descricao = pegar_descricao()
    valor = pegar_valor()
    tipo_lancamento = pegar_tipo()
    data_lancamento = validar_data()
    categoria_lancamento = categoria.get()

    if descricao is None or valor is None or tipo_lancamento is None or data_lancamento is None or categoria_lancamento == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos antes de cadastrar")
        return

    inserir_lancamento(descricao, valor, tipo_lancamento, data_lancamento, categoria_lancamento)

    entrada_descricao.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    tipo.set("")

    messagebox.showinfo("Sucesso", "Lançamento cadastrado com sucesso!")


    

janela = tk.Tk()
janela.title("Controle Financeiro")

tk.Label(janela, text="Descrição").pack()

entrada_descricao = tk.Entry(janela)
entrada_descricao.pack()

tk.Label(janela, text="Valor").pack()

entrada_valor = tk.Entry(janela)
entrada_valor.pack()

tk.Label(janela, text="Data").pack()

entrada_data = tk.Entry(janela)
entrada_data.pack()

entrada_data.insert(0,date.today().strftime("%d/%m/%Y"))


tk.Label(janela, text="Tipo").pack()

tipo = ttk.Combobox(janela, values=["Entrada", "Saída"])
tipo.pack()

tk.Label(janela,text="Categoria").pack()
categoria = ttk.Combobox(janela,values=["Alimentação", "Transporte", "Moradia", "Lazer", "Saúde", "Outros"])
categoria.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack()

tk.Label(janela,text="Lançamentos").pack()
tabela = ttk.Treeview(janela, columns=("id", "descricao", "valor", "tipo", "data", "categoria"), show="headings")

tabela.heading("id", text="ID")
tabela.heading("descricao", text="Descrição")
tabela.heading("valor", text="Valor")
tabela.heading("tipo", text="Tipo")
tabela.heading("data", text="Data")
tabela.heading("categoria", text="Categoria")

tabela.pack()


janela.mainloop()