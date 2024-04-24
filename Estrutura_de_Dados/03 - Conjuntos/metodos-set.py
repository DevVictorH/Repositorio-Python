## set.union ou {}union - serve para unir um conjunto em outro
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))


## set.intersection ou {}intersection - serve para ver partes iguais
conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 4}
print(conjunto_a.intersection(conjunto_b))

## set.difference ou {}difference - mostra o que tem de diferente
conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 4}
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

## set.symetric_difference ou {}symetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 4}
print(conjunto_a.symmetric_difference(conjunto_b))

## set.issubset ou {}issubset - mostra se todos os elementos de um grupo pertence ao outro
conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 4, 1, 6}
print(conjunto_a.issubset(conjunto_b))

## set.issuperset ou {}issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 4, 1}
print(conjunto_a.issuperset(conjunto_b))

## set.isdisjoint ou {}isdisjoint - mostra se todos os elementos de um conjunto não estão presente em outro conjunto
conjunto_a = {1, 2, 3}
conjunto_b = {6, 5, 7}
print(conjunto_a.isdisjoint(conjunto_b))

## set.add - adiciona um elemento no conjunto, mas se o elemento ja existir ele vai ignorar
conjunto_a = {1, 2, 3}
conjunto_a.add(25)
print(conjunto_a)

## set.clear - vai limpar o conjunto
conjunto_a = {1, 2, 3}
print(conjunto_a.clear())

## set.copy - vai copiar o conjunto
conjunto_a = {1, 2, 3}
conjunto_a.copy()

## set.discard - descarta um valor do conjunto
conjunto_a = {1, 2, 3, 256, 35, 32}
conjunto_a.discard(256)
print(conjunto_a)

## set.pop - tira o valor da frente do conjunto
conjunto_a = {1, 2, 3, 4, 6}
conjunto_a.pop()
print(conjunto_a)

## set.remove - remove um valor, mas voce pode escolher o valor
conjunto_a = {1, 2, 3, 4, 6}
conjunto_a.remove(3)
print(conjunto_a)

## len - mostra quantos valores tem dentro do conjunto
conjunto_a = {1, 2, 3, 4, 6}
print(len(conjunto_a))

