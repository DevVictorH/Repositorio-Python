class passaro:
    def voar(self):
        print("voando...")

class pardal(passaro):
    def voar(self):
        return super().voar()
    

class avestruz(passaro):
    def voar(self):
        print("avestruz não voa")

# Exemplo ruim de herança para "ganhar" o metodo voar
class aviao(passaro):
    def voar(self):
        print("O aviao esta decolando...")

def plano_de_voo(objeto):
    objeto.voar()


plano_de_voo(pardal())
plano_de_voo(avestruz())
plano_de_voo(aviao())