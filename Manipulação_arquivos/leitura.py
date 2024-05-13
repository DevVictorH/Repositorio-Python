arquivo = open("C:\CursoPy\Manipulação_arquivos\lorem.txt", "r")
print(arquivo.read())
#print(arquivo.readline())
#print(arquivo.readlines())

# Dica de gerador
# while len(linha := arquivo.readline()):
#    print(linha)

arquivo.close()
