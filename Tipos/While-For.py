# for
texto = ''
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()

# Range Built-in
# range(0 = start, 10 = stop, 2 = step [opcional])
print(list(range(0, 11, 2)))

# Range dentro do for
for numero in range(0, 51, 5):
    print(numero, end=" ")
print()

# While
opcao = -1

while opcao != 0:
    opcao = int(input(" [1] Sacar \n [2] Extrato \n [3] Sair \n"))
    
    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo extrato")
    elif opcao == 3:
        print("Saindo")
        break
    else:
        print("Opcao invalida")
    