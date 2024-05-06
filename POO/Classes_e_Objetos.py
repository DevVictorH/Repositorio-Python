class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor    
        self.modelo = modelo    
        self.ano = ano    
        self.valor = valor    
    
    def buzinar(self):
        print("PLIM PLIM PLIM")

    def parar(self):
        print("Parando a bicicleta")

    def correr(self):
        print("Vruuuuum")

    #def __str__(self):
    #    return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"


bike1 = Bicicleta("vermelho", "caloi", 2024, 600)
bike1.buzinar()
bike1.correr()
print(bike1.cor, bike1.modelo, bike1.valor)

bike2 = Bicicleta("azul", "monark", 2000, 1000)
bike2.buzinar()

print(bike2)
    