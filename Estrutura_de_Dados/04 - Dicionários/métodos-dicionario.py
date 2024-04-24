## dict.fromkeys ou {}fromkeys - adiciona novas chaves de uma vez ou cria um dicionario com valor vazio
contatos = dict.fromkeys(["nome", "telefone"])
contatos = dict.fromkeys(["nome", "telefone"], "vazio")
print(contatos)

## dict.get - serve para procurar um valor e caso ele não exista voce pode definir um valor padrao pra retornar
contatos = {"contatos": {"nome": "Victor"}}
print(contatos.get("chave"))
print(contatos.get("chave", "vazio"))

## dict.items - 
contatos = {"contatos": {"nome": "Victor"}}
print(contatos.items())

## dict.keys - retorna so as chaves do dicionario
contatos = {"contatos": {"nome": "Victor"}, "contatos2": {"nome": "Joao"}}
print(contatos.keys())

## dict.pop - remove uma chave do dicionario
contatos = {"contatos": {"nome": "Victor"}, "contatos2": {"nome": "Joao"}}
contatos.pop("contatos")
print(contatos)

## dict.popitem
contatos = {"contatos": {"nome": "Victor"}, "contatos2": {"nome": "Joao"}}
contatos.popitem()
print(contatos)

## setdefault - coloca uma chave como padrao, se a chave ja existir ele não faz nada
contatos = {"contatos": {"nome": "Victor"}, "contatos2": {"nome": "Joao"}}
contatos.setdefault("telefone", "555-666")
print(contatos)

## dict.update - atualizar o valor de alguma chave
contatos = {"contatos": {"nome": "Victor", "idade": 18}, "contatos2": {"nome": "Joao"}}
contatos.update({"contatos": {"nome": "Pedro"}})
print(contatos)

## dict.values - retorna o valor das chaves
contatos = {"contatos": {"nome": "Victor", "idade": 18}, "contatos2": {"nome": "Joao"}}
print(contatos.values())

## in - serve para verificar se uma chave existe ou não no dicionário
contatos = {"contatos": {"nome": "Victor", "idade": 18}, "contatos2": {"nome": "Joao"}}
print("telefone" in contatos["contatos"])
print("nome" in contatos["contatos"])

## del - retira um valor
contatos = {"contatos": {"nome": "Victor", "idade": 18}, "contatos2": {"nome": "Joao"}}
del contatos["contatos"]["nome"]
del contatos["contatos2"]
print(contatos)