from pathlib import Path

ROOTH_PATH = Path(__file__).parent

# with - garante que o arquivo seja fechado automaticamente
with open(ROOTH_PATH / "lorem.txt", "r") as arquivo:
    print("avc")

try:
    with open("abc.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Error ao abrir o arquivo {exc}")

# encoding - tipo de codificação do arquivo
try:
    with open(ROOTH_PATH / "new_file.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Teste de escrita")
except IOError as exc:
    print(f"Error ao tentar abrir o arquivo: {exc}")









