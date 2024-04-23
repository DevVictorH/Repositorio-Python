deposito = 0
saque = 0
extrato = ""
saldo = 0
LIMITE_SAQUE = 3
limite = 500
numero_saque = 0

while True:
    print(""" 
    -------- Sistema Bancário --------
      1) Depósito
      2) Saque
      3) Extrato
      4) Sair
          
      O que você deseja fazer?""")
    
    opcao = int(input())

    if opcao == 1:
        print("Você deseja depositar quanto?")
        deposito = float(input())
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de R${deposito}\n"
            print("Depósito feito com sucesso")
        else: print("Valor inválido")
    elif opcao == 2:
        if numero_saque == LIMITE_SAQUE:
            print("Limite de saque diário atingido")
            continue
        else:print("Você deseja sacar quanto?")
        saque = float(input())
        if saque < 0:
            print("Valor de saque inválido")
            continue
        if saque <= saldo and saque > 0 and saque <= 500:
            saldo -= saque
            print("Saque realizado com sucesso")
            numero_saque += 1
            extrato += f"Saque de R${saque}\n"
        else: print("Saldo insuficiente")
        
    elif opcao == 3:
        print("------ Extrato ------")
        print(extrato)
        print(f"Seu saldo é de R${saldo}")
        print("----------------------")
    elif opcao == 4:
        print("Saindo...")
        break
    else: print("Opção inválida")


