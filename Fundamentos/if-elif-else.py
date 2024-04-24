idade = int(input("Quantos anos voce tem?\n"))

if idade >= 18:
    print("Voce é maior de idade")
else:
    print("Voce é menor de idade")

conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 2000
cheque_especial = 500

# if aninhado
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sussesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o cheque especial")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado")
    else:
        print("Saldo insuficiete")
else:
    print("Sistema não reconheceu a conta")

#if ternario
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")