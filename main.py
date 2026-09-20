import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

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

def cadastrar():
    descricao = pegar_descricao()
    valor = pegar_valor()
    tipo_lancamento = pegar_tipo()

    if descricao is None or valor is None or tipo_lancamento is None:
        messagebox.showwarning("Atenção", "Preencha todos os campos antes de cadastrar")
        return

    print(descricao)
    print(valor)
    print(tipo_lancamento)

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

tk.Button(janela, text="Cadastrar", command=cadastrar).pack()


janela.mainloop()