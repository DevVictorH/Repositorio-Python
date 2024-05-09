def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("Faz algo dps de executar")
    return envelope

@meu_decorador    
def ola_mundo():
    print("Ola mundo")


## ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
