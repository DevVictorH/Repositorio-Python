def calcular(operacao):
    def soma(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    if operacao == "+":
        return soma
    else:
        return subtrair

resultado = calcular("+")(10, 5)
print(resultado)