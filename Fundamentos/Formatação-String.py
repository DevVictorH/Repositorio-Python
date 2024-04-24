nome = "Victor"
idade = 18
profissao = "programador"
dados = {"nome": "Victor", "idade": 18}
saldo = 25.678987

print(f"Meu nome é {nome}, tenho {idade} anos e sou {profissao}") ## Metodo mais utilizado
print("Meu nome é %s, tenho %d anos e sou %s" % (nome, idade, profissao)) ## Modo old style, não é utilizado
print("Meu nome é {nome}, tenho {idade} anos e sou {profissao}".format(nome=nome, idade=idade, profissao=profissao)) ## Metodo .format
print("Meu nome é {}, tenho {} anos e sou {}".format(nome, idade, profissao)) ## Metodo .format
print("Meu nome é {0}, tenho {1} anos e sou {2}".format(nome, idade, profissao)) ## Metodo .format
print("nome: {nome} idade: {idade}".format(**dados))
print(f"saldo: {saldo:.2f}")

print(f"""Meu nome é {nome} 
Eu tenho {idade} anos
E sou {profissao}""") ## String de multiplas linhas ou String tripla
