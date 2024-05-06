## Deve usar underline para fazer a convenção e deixar o atributo como privado

class conta:
    def __init__(self, nmr_agencia, saldo=0):
        self._saldo = saldo
        self.nmr_agencia = nmr_agencia

    def sacar(self, valor):
        self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor

    def mostrar_saldo(self):
        return self._saldo


conta = conta("0001", 100)
print(conta._saldo)
print(conta.mostrar_saldo())