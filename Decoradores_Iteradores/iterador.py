# Um iterador é um objeto que implementa next, que deve retornar 
# o próximo elemento do objeto iterável que o retornou e gerar 
# uma exceção StopIteration 

class meu_iterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero *2
        except IndexError:
            raise StopIteration
        

for i in meu_iterador(numeros=[4, 8, 10]):
    print(i)