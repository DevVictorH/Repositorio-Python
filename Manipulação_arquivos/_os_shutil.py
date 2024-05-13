import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criar um arquivo ou pasta
# os.mkdir(ROOT_PATH / "Novo diretorio")


arquivo = open(ROOT_PATH / "novo_arquivo.txt", "w")
arquivo.close()


# Renomear um arquivo
os.rename(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "novo_nome.txt")


# Remover um arquivo
os.remove(ROOT_PATH / "novo_arquivo.txt")


# Mover o arquivo
shutil.move(ROOT_PATH / "novo_nome.txt", ROOT_PATH / "novo diretorio")

