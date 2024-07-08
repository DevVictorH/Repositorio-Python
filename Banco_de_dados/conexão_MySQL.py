import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cadastro"
  )


if mydb.is_connected():
    print("Conexão estabelecida com sucesso!")
    cursor = mydb.cursor()

def inserir_informacao():  
    data = ('Julia', 'F') 
    cursor.execute("INSERT INTO pessoas(nome, sexo) VALUES(%s, %s);", data)
    mydb.commit()

def deletar_linha(mydb, cursor):
    data = (id, )
    cursor.execute("DELETE FROM pessoas WHERE id = '4';")
    mydb.commit()

def inserir_varias_informacoes(mydb, cursor, dados):
    cursor.executemany("INSERT INTO pessoas(nome, peso) VALUES(%s, %s);", dados)
    mydb.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM pessoas WHERE id =%s;", (id, ))
    resultado = cursor.fetchone()
    return resultado

def listar_cliente(cursor):
    return cursor.execute("SELECT * FROM pessoas ORDER BY nome;")

cliente = recuperar_cliente(cursor, 1)
clientes = listar_cliente(cursor)
for cliente in clientes:
    print(cliente)

dados = [
    ("Guilherme", "82.2"),
    ("Rafael", "74.4"),
    ("Leticia", "62.1")
]

# deletar_linha(mydb, cursor)
# inserir_varias_informacoes(mydb, cursor, dados)



