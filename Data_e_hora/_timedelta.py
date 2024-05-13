from datetime import datetime, timedelta, time

data = datetime(2024, 5, 9, 11, 47)
print(data)

data = data + timedelta(weeks=1)
print(data)

tipo_carro = "G"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"\no carro chegou {data_atual} e ficará pronto às {data_estimada}")

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"\no carro chegou {data_atual} e ficará pronto às {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"\no carro chegou {data_atual} e ficará pronto às {data_estimada}")

result = datetime(2024, 4, 26, 11, 19, 0) - timedelta(hours=1)
print(result.time())    