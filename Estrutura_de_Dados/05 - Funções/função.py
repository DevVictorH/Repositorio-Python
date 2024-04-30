## def - para criar função

def mensagem():
    print("Hello world")

mensagem()

def mensagem2(nome):
    print(f"Ola {nome}")

mensagem2("Victor")

def mensagem3(nome="Anonimo"):
    print(f"Olá {nome}")

mensagem3()

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1    
    return antecessor, sucessor

print(calcular_total([1, 5, 10, 15]))
print(retorna_antecessor_e_sucessor(10))


def salvar_carro(marca, modelo, ano, placa):
    print(f"{marca}, {modelo}, {ano}, {placa}")

salvar_carro(marca="BMW", modelo="X1", ano=2020, placa="555-666")
salvar_carro(**{"marca":"BMW", "modelo":"X1", "ano":"2020", "placa":"555-666"}) #  ** - transforma em um dicionário

