frutas = []
print(frutas)

frutas = ["laranja", "maçã", "uva"]
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrario", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print(frutas[2])

matriz = [
    [1, "a", 2],
    [5, "b", -9],
    [-2, 0, "c"]
]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][2])
print(matriz[1][0])

lista = "python"
print(lista[::])
print(lista[:4])
print(lista[::-1])
print(lista[0:6:2])

carros = ["gol", "onix", "hb20"]
for car in carros:
    print(car)

for i, car in enumerate(carros):
    print(f"{i}: {carros}")

numeros = [1, 30, 20, 15, 25, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(numero)
        
