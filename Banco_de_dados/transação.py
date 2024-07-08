import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cadastro"
  )

cursor = mydb.cursor()


if mydb.is_connected():
    print("Conexão estabelecida com sucesso!")
    cursor = mydb.cursor()
try:
    cursor.execute("INSERT INTO pessoas(nome, sexo) VALUES(%s, %s)", ("teste2", "F"))
    cursor.execute("INSERT INTO pessoas(id, nome, sexo) VALUES(%s, %s)", ("2", "teste2", "F"))
except Exception as e:
    print(f"Ops, ocorreu um erro: {e}")
    mydb.rollback()    


