import os
import json


def adicionar_pasta(biblioteca, caminho_pasta, descricao):
    pasta_info = {
        "caminho": caminho_pasta,
        "descricao": descricao
    }
    biblioteca.append(pasta_info)
    salvar_biblioteca(biblioteca)
    print(f"Pasta '{descricao}' adicionada à biblioteca.")


def remover_pasta(biblioteca, indice):
    if 0 <= indice < len(biblioteca):
        pasta_removida = biblioteca.pop(indice)
        salvar_biblioteca(biblioteca)
        print(f"Pasta '{pasta_removida['descricao']}' removida da biblioteca.")
    else:
        print("Índice inválido.")


def listar_pastas(biblioteca):
    for i, pasta in enumerate(biblioteca):
        print(f"{i}. {pasta['descricao']} - {pasta['caminho']}")


def salvar_biblioteca(biblioteca):
    with open("biblioteca_pastas.json", "w") as arquivo:
        json.dump(biblioteca, arquivo)


def carregar_biblioteca():
    if os.path.exists("biblioteca_pastas.json"):
        with open("biblioteca_pastas.json", "r") as arquivo:
            return json.load(arquivo)
    else:
        return []


biblioteca_pastas = carregar_biblioteca()

while True:
    print("\nBiblioteca de Pastas")
    print("1. Adicionar Pasta")
    print("2. Remover Pasta")
    print("3. Listar Pastas")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        caminho = input("Digite o caminho da pasta: ")
        descricao = input("Digite uma descrição para a pasta: ")
        adicionar_pasta(biblioteca_pastas, caminho, descricao)
    elif escolha == "2":
        listar_pastas(biblioteca_pastas)
        indice = int(input("Digite o índice da pasta que deseja remover: "))
        remover_pasta(biblioteca_pastas, indice)
    elif escolha == "3":
        listar_pastas(biblioteca_pastas)
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")


salvar_biblioteca(biblioteca_pastas)

print("Programa encerrado.")
