def cria_carro(modelo, ano, placa, /, marca, motor, combustivel):  # tudo antes da barra tem que ser definido por posição e o que vem dps
    print(modelo, ano, placa, marca, motor, combustivel)            # da barra pode ser definido por posição ou nomeado.

cria_carro("palio", 1990, "ABC-222", marca="fiat",  motor = 1.0, combustivel="gasolina")

def cria_carro2(*, modelo, ano, marca, motor, combustivel):
    print(modelo, ano, marca, motor, combustivel)

cria_carro2(modelo="PALIO", ano=1992, marca="fiat", motor=1.0, combustivel="gasolina")

def cria_carro3(modelo, ano, /,*, marca, motor, combustivel):
    print(modelo, ano, marca, motor, combustivel)

cria_carro3("PALIO", 1992, marca="fiat", motor=1.0, combustivel="gasolina")

def somar(a, b):
    return a+b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, somar):
    resultado = somar(a, b)
    print(f"O resultado de {a} + {b} é {resultado}")

exibir_resultado(10, 10, somar)

operacao = somar
print(operacao(10, 30))

