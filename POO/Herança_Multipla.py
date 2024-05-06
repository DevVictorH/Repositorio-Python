class animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"

class mamifero(animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class ave(animal):
    def __init__(self,  cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class cachorro(mamifero):
    pass

class gato(mamifero):
    pass

class leao(mamifero):
    pass

class onitorrinco(mamifero, ave):
    def __init__(self, cor_pelo, cor_bico, numero_patas, **kw):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas, **kw)
        print(onitorrinco.__mro__)

Gato = gato(numero_patas=4, cor_pelo="preto")
print(Gato)


Onitirrinco = onitorrinco(numero_patas=5, cor_pelo="vermelho", cor_bico="azul")
print(Onitirrinco)