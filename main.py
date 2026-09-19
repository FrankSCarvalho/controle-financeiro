import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Controle Financeiro")

tk.Label(janela, text="Descrição").pack()

entrada_descricao = tk.Entry(janela)
entrada_descricao.pack()

tk.Label(janela, text="Valor").pack()

entrada_valor = tk.Entry(janela)
entrada_valor.pack()

tk.Label(janela, text="Tipo").pack()

tipo = ttk.Combobox(janela, values=["Entrada", "Saída"])
tipo.pack()

tk.Button(janela, text="Cadastrar").pack()

janela.mainloop()