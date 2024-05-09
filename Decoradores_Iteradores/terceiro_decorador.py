def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo dps de executar")
        return resultado
    return envelope

@meu_decorador    
def ola_mundo(nome):
    print(f"Ola mundo {nome}")
    return nome.upper()


resultado = ola_mundo("Victor")
print(resultado)