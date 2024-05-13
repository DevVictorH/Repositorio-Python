from pathlib import Path

ROOTH_PATH = Path(__file__).parent


try:
    arquivo = open("python.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print("Não foi possivel abrir o arquivo!")
    print(exc)
except Exception as exc:
    print(f"Algum erro ocorreu ao tentar abrir o arquivo: {exc}")

    

