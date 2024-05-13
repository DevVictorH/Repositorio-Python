escrita = open("C:\CursoPy\Manipulação_arquivos/teste.txt", "w")
escrita.write("Escrevendo dados em um novo arquivo.")
escrita.writelines(["\n" "Python", " escrevendo", " um ", "texto"])

escrita.close()