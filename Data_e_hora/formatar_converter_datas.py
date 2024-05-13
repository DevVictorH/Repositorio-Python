from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "26/04/2006 00:00:00"
mascara_ptbr = "%d/%m/%Y %H:%M:%S"

# fazer uma formatação de data e hora
print(data_hora_atual.strftime(mascara_ptbr))

# converter uma string para data e hora
data = datetime.strptime(data_hora_string, mascara_ptbr)
print(data.strftime(mascara_ptbr))
