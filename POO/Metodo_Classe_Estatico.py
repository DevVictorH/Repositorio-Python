class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod ## Metodo de classe = usado quando você precisa ter acesso ao conteudo da classe.
    def get_data_nascimento(cls, dia, mes, ano, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod ## Metodo estatico = usado quando você não precisa de contexto nem do conteudo da classe.
    def e_maior_idade(idade):
        if idade >= 18:
            return print("É maior de idade.")
        else:
            return print("É menor de idade.")
    
    def __str__(self):
        return f"Meu nome é {self.nome} e eu tenho {self.idade} anos."
    
p1 = pessoa.get_data_nascimento(26, 4, 2006, "Victor")
print(p1)

p1.e_maior_idade(16)