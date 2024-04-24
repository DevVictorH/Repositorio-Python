pessoa = {"nome": "Victor", "idade": 18}
pessoa = dict(nome= "Victor", idade=18)
pessoa["telefone"] = "555-333"
print(pessoa)

print(pessoa["nome"])
pessoa["nome"] = "Luiz"
print(pessoa["nome"])

contatos = {
    "cliente1": {"nome": "Victor", "telefone" : "555-666"},
    "cliente2": {"nome": "joão", "telefone" : "333-666"},
    "cliente3": {"nome": "Vinicius", "telefone" : "444-666"}
}

print(contatos["cliente1"]["telefone"])

for cliente in contatos:
    print(cliente, contatos[cliente])

for cliente, valor in contatos.items():
    print(cliente, valor)

    