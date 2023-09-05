import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil

def adicionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    descricao = descricao_entry.get()

    if pasta_selecionada and descricao:
        pasta_info = {
            "caminho": pasta_selecionada,
            "descricao": descricao
        }
        biblioteca_pastas.append(pasta_info)
        salvar_biblioteca()
        atualizar_lista()
        messagebox.showinfo("Sucesso", f"Pasta '{descricao}' adicionada à biblioteca.")
    else:
        messagebox.showerror("Erro", "Por favor, selecione uma pasta e preencha a descrição.")

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

def visualizar_pasta():
    selecionado = lista_pastas.curselection()

    if selecionado:
        indice = selecionado[0]
        pasta_selecionada = biblioteca_pastas[indice]
        pasta_caminho = pasta_selecionada["caminho"]
        os.startfile(pasta_caminho)  # Abre a pasta no explorador de arquivos padrão

def atualizar_lista():
    lista_pastas.delete(0, tk.END)
    for pasta in biblioteca_pastas:
        lista_pastas.insert(tk.END, pasta['descricao'])

def salvar_biblioteca():
    with open("biblioteca_pastas.json", "w") as arquivo:
        json.dump(biblioteca_pastas, arquivo)

def carregar_biblioteca():
    if os.path.exists("biblioteca_pastas.json"):
        with open("biblioteca_pastas.json", "r") as arquivo:
            return json.load(arquivo)
    else:
        return []

biblioteca_pastas = carregar_biblioteca()

janela = tk.Tk()
janela.title("Biblioteca de Pastas")

descricao_label = tk.Label(janela, text="Descrição:")
descricao_entry = tk.Entry(janela, width=40)
adicionar_botao = tk.Button(janela, text="Adicionar Pasta", command=adicionar_pasta)
remover_botao = tk.Button(janela, text="Remover Pasta", command=remover_pasta)
visualizar_botao = tk.Button(janela, text="Visualizar Pasta", command=visualizar_pasta)
lista_pastas = tk.Listbox(janela, width=60, height=15)
atualizar_lista()

descricao_label.grid(row=0, column=0, padx=10, pady=5)
descricao_entry.grid(row=0, column=1, padx=10, pady=5)
adicionar_botao.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
remover_botao.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
visualizar_botao.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
lista_pastas.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

janela.mainloop()
