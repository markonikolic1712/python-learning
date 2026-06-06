# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# day,temp,condition
# Monday,12,Sunny
# Tuesday,14,Rain
# Wednesday,15,Rain
# Thursday,14,Cloudy
# Friday,21,Sunny
# Saturday,22,Sunny
# Sunday,24,Sunny

import pandas
from numpy.ma.core import count
from pandas.core.array_algos.masked_accumulations import cumsum

data = pandas.read_csv("weather_data.csv")
print(type(data)) # <class 'pandas.DataFrame'> - u pandas dokumentaciji za pandas.DataFrame pise da je tip tabela
print(type(data["temp"])) # <class 'pandas.Series'>
# print(data) # svi podaci
# print(data["temp"]) # podaci u kolini temp
# u pandas biblioteci postoje dve vrse podataka: DataFrame i Series. DataFrame je tabela a Series je lista podataka koja je u stvari kolona sa podacima u tabeli

# konvertovanje podataka u dictionary - koristi se pandas metoda to_dict()
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
data_dict = data.to_dict()
print(data_dict)

# Series podatak se konveruje u listu
# [12, 14, 15, 14, 21, 22, 24]
print(data["temp"].to_list())

# izracunavanje prosecne temperature
avg_temp = sum(data["temp"].to_list()) / len(data["temp"].to_list())
print(avg_temp)
# izracunavanje prosecne temperature uz pomoc pandas metoda
print(data["temp"].mean())

# u pozadini pandas konvertuje tabelu u objekat pa do kolone moze da se dodje kao da je atribut
# ovo je case sensitive pa mora da se pazi na velika i mala slova
# isto je kada se kolona uzima sa data["condition"]
print(data.condition)

print("\n****** uzimanje reda iz tabele ******")
# ovo bi bilo: select * from data where day = "Monday"
print(data[data.day == "Monday"])

print("\n****** uzimanje reda sa maksimalnom temperaturom ******")
print(data[data.temp == data.temp.max()])

print("\n****** uzimanje temp za red sa Monday ******")
# ceo red se setuje u varijablu monday
monday = data[data.day == "Monday"]
# konvertovanje C u F
print(monday.temp * 9/5 + 32)


print("\n****** kreiranje dataframe-a (tabele) ******")
# kreira se dataframe od podataka koje imamo - od dictionary-a
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# poziva se DataFrame iz pandas biblioteke
data_from_dict = pandas.DataFrame(data_dict)
print(data_from_dict)
# sada tpodatke iz dataframe spustamo u csv fajl
# index=False - ovaj parametar se koristi da se index ne bi dodao kao prva kolona
data_from_dict.to_csv("students", index=False)












