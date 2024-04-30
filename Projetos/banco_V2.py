deposito = 0
saque = 0
extrato = ""
saldo = 0
LIMITE_SAQUE = 3
limite = 500
AGENCIA = "0001"
numero_saque = 0
contas=[]
usuarios=[]
numero_conta=0

def depositar(saldo, deposito, extrato, /):
    print("Você deseja depositar quanto?")
    deposito = float(input())
    if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de R${deposito}\n"
            print("Depósito feito com sucesso")
    else: print("Valor inválido")
    return saldo, extrato

def sacar( saldo, valor, extrato, limite, limite_saque, numero_saque):
    excedeu_saques = numero_saque > limite_saque
    if excedeu_saques:
            print("limite de saque diário atingido")
    else:print("Você deseja sacar quanto?")
    valor = float(input())
    if valor < 0:
            print("Valor de saque inválido")
    
    if valor <= saldo and valor > 0 and valor <= limite:
            saldo -= valor
            numero_saque += 1
            print("Saque realizado com sucesso")
            
            print(numero_saque)
            extrato += f"Saque de R${valor}\n"
    else: print("Saldo insuficiente")
    return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):
    print("------ Extrato ------")
    print(extrato)
    print(f"Seu saldo é de R${saldo}")
    print("----------------------")

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, criação de conta encerrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    nome = input("Digite o nome de usuário: ")
    data_nascimento = input("Digite sua data de nascimento (dd - mm - aaaa): ")
    endereco = input("Digite seu endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("--- Usuario criado com sucesso! ---")
    
def listar_contas(contas):
     for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(linha)


while True:
    print(""" 
    -------- Sistema Bancário --------
      1) Depósito
      2) Saque
      3) Extrato
      4) Criar Usuario
      5) Criar Conta Corrente
      6) Lista de contas  
      7) Sair
          
      O que você deseja fazer?""")
    
    opcao = int(input())

    if opcao == 1:
        saldo, extrato = depositar(saldo, deposito, extrato)
    elif opcao == 2:
      saldo, extrato = sacar(saldo = saldo, valor=saque, extrato=extrato, limite=limite, limite_saque=LIMITE_SAQUE, 
                             numero_saque=numero_saque)   
        
    elif opcao == 3:
        exibir_extrato(saldo, extrato=extrato)
    
    elif opcao == 4:
        criar_usuario(usuarios)

    elif opcao == 5:  
        numero_conta = len(contas) +1
        conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

        if conta:
             contas.append(conta)
    elif opcao == 6:
        listar_contas(contas)
        
    elif opcao == 7:
         print("Saindo...")
         break
    
    else: print("Opção inválida")


