from abc import ABC, abstractmethod  ## classe abstrata - vai te obrigar a passar os metodos para outra classe

class controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class controle_tv(controle_remoto):
    def ligar(self):
        print("Ligando...")

    def desligar(self):
        print("Desligando...")

class controle_ar_condicionado(controle_remoto):
    def ligar(self):
        print("Ligando o ar condicionado...")

    def desligar(self):
        print("Desligando o ar condicionado...")

controle = controle_tv()
controle.ligar()
controle.desligar()

controle = controle_ar_condicionado()
controle.ligar()
controle.desligar()
