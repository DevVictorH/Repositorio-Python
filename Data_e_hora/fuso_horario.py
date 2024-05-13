from datetime import datetime, timedelta, timezone

data = datetime.now(timezone(timedelta(hours=2)))
data_SP =  datetime.now(timezone(timedelta(hours= -3)))

print(data)
print(data_SP)