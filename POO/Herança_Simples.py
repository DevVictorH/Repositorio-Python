class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")
        
    def __str__(self):
        return f"{self.__class__.__name__}: cor = {self.cor}, placa = {self.placa}, numero de rodas = {self.numero_rodas}"

class moto(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    pass

motocicleta = moto("verde", 5235, 2)
print(motocicleta)
motocicleta.ligar_motor()

car = carro("azul", 8421, 4)
print(car)
car.ligar_motor()

truck = caminhao("laranja", 4214, 8)
print(truck)
truck.ligar_motor()