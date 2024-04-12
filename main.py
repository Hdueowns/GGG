from datetime import datetime

# Создание объекта datetime для 4 ноября 2020 г., 14:53:00
dt = datetime(2020, 11, 4, 14, 53, 0)

# Вывод в соответствующих форматах
print(dt.strftime("%Y/%m/%d %H:%M:%S"))  # 2020/11/04 14:53:00
print(dt.strftime("%y/%B/%d %I:%M:%S %p"))  # 20/Ноябрь/04 02:53:00 PM
print(dt.strftime("%a, %Y %b %d"))  # Wed, 2020 Nov 04
print(dt.strftime("%A, %Y %B %d"))  # Среда, 2020 Ноябрь 04
print("Weekday:", dt.strftime("%w"))  # Будний день: 3
print("Day of the year:", dt.strftime("%j"))  #День в году: 309
print("Week number of the year:", dt.strftime("%U"))  # Номер недели в году: 44
