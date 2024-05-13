import csv
from pathlib import Path

ROOTH_PATH = Path(__file__).parent

try:
    with open(ROOTH_PATH / "arquivo_novo.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Victor"])
        escritor.writerow(["2", "João"])
        escritor.writerow(["3", "Luiz"])

except IOError as exc:
    print(f"Error ao criar o arquivo: {exc}")

try:
    with open(ROOTH_PATH / "arquivo_novo.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)

except IOError as exc:
    print(f"Error ao criar o arquivo: {exc}")


try:
    with open(ROOTH_PATH / "arquivo_novo.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f"ID:  {row["id"]}")
            print(f"Nome: {row["nome"]}")

except IOError as exc:
    print(f"Error ao criar o arquivo: {exc}")

