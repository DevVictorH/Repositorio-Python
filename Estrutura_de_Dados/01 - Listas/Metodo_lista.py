## [].append adiciona um valor na lista 

lista = []
lista.append(1)
lista.append(["victor", 10, 20])
print(lista)

l2 = lista.copy() ## copia um objeto, porem o que vc alterar na copia nao altera o original
l2[0] = 2
print(lista)
print(l2)

lista.clear() ## limpa a lista
print(lista)

## [].count
cores = ["vermelho", "azul", "verde"]
cores.count("vermehlo")
print(cores.count("azul"))

## [].extend - serve para juntar uma lista em outra
linguagens = ["python", "java"]
print(linguagens)
linguagens.extend(["c++", "html"])
print(linguagens)

## [].index - ele acha a primeira ocorrencia/posição que o objeto aparece na sua lista
print(linguagens.index("java"))

## [].pop - remove o ultimo objeto colocado
print(linguagens.pop())
print(linguagens)

## [].remove - remove um objeto
linguagens.remove("c++")
print(linguagens)

## [].sort - ordena a lista alfabeticamente
linguagens.sort()
print(linguagens)
linguagens.sort(reverse = True)
print(linguagens)

## [].reverse - deixa a lista de trás pra frente
linguagens.reverse()
print(linguagens)

## len - mostra o tamanho da lista
print(len(linguagens))



