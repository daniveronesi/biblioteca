import os
import json
import tkinter as tk
from tkinter import messagebox

# Função para adicionar uma pasta à biblioteca
def adicionar_pasta():
    caminho = caminho_entry.get()
    descricao = descricao_entry.get()

    if caminho and descricao:
        pasta_info = {
            "caminho": caminho,
            "descricao": descricao
        }
        biblioteca_pastas.append(pasta_info)
        salvar_biblioteca()
        atualizar_lista()
        messagebox.showinfo("Sucesso", f"Pasta '{descricao}' adicionada à biblioteca.")
    else:
        messagebox.showerror("Erro", "Por favor, preencha ambos os campos.")

# Função para remover uma pasta da biblioteca
def remover_pasta():
    selecionado = lista_pastas.curselection()

    if selecionado:
        indice = selecionado[0]
        pasta_removida = biblioteca_pastas.pop(indice)
        salvar_biblioteca()
        atualizar_lista()
        messagebox.showinfo("Sucesso", f"Pasta '{pasta_removida['descricao']}' removida da biblioteca.")
    else:
        messagebox.showerror("Erro", "Selecione uma pasta para remover.")

# Função para listar todas as pastas na biblioteca
def atualizar_lista():
    lista_pastas.delete(0, tk.END)
    for pasta in biblioteca_pastas:
        lista_pastas.insert(tk.END, pasta['descricao'])

# Função para salvar a biblioteca em um arquivo JSON
def salvar_biblioteca():
    with open("biblioteca_pastas.json", "w") as arquivo:
        json.dump(biblioteca_pastas, arquivo)

# Função para carregar a biblioteca de um arquivo JSON
def carregar_biblioteca():
    if os.path.exists("biblioteca_pastas.json"):
        with open("biblioteca_pastas.json", "r") as arquivo:
            return json.load(arquivo)
    else:
        return []

# Programa principal
biblioteca_pastas = carregar_biblioteca()

# Criar a janela principal
janela = tk.Tk()
janela.title("Biblioteca de Pastas")

# Widgets
caminho_label = tk.Label(janela, text="Caminho da Pasta:")
caminho_entry = tk.Entry(janela, width=40)
descricao_label = tk.Label(janela, text="Descrição:")
descricao_entry = tk.Entry(janela, width=40)
adicionar_botao = tk.Button(janela, text="Adicionar Pasta", command=adicionar_pasta)
remover_botao = tk.Button(janela, text="Remover Pasta", command=remover_pasta)
lista_pastas = tk.Listbox(janela, width=60, height=15)
atualizar_lista()

# Layout
caminho_label.grid(row=0, column=0, padx=10, pady=5)
caminho_entry.grid(row=0, column=1, padx=10, pady=5)
descricao_label.grid(row=1, column=0, padx=10, pady=5)
descricao_entry.grid(row=1, column=1, padx=10, pady=5)
adicionar_botao.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
remover_botao.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
lista_pastas.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Loop da interface
janela.mainloop()
