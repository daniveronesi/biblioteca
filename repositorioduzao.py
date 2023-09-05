import os
import shutil

diretorio_origem = "/caminho/para/a/pasta/de/origem"

diretorio_destino = "/caminho/para/a/pasta/de/destino"

if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)

arquivos = os.listdir(diretorio_origem)

for arquivo in arquivos:
    
    caminho_completo = os.path.join(diretorio_origem, arquivo)

    if os.path.isfile(caminho_completo):
        
        extensao = arquivo.split(".")[-1]

        diretorio_extensao = os.path.join(diretorio_destino, extensao)
        if not os.path.exists(diretorio_extensao):
            os.makedirs(diretorio_extensao)

        shutil.move(caminho_completo, os.path.join(diretorio_extensao, arquivo))

print("Organização concluída!")
