class bola:
    def __init__(self, cor, profissional=False):
        self.cor = cor
        self.profissional = profissional

    def chutar(self):
        print("Você chutou a bola")

    def pro(self, profissional):
        if profissional:
            print("bola não profissional")
        else:
            print("Bola profissional")

class bola2(bola):
    pass

futebol = bola("verde")
futebol.chutar()
print(futebol.cor)
futebol.pro(True)

fut = bola2("azul")

print(fut.cor)

print(len("agua"))
print(len([10, 20, 30]))