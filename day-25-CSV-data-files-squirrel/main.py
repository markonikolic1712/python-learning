import pandas

# zadatak je da se uzmu podaci iz Squirrel_Data.csv i da se prebroji koliko ima veverica po bojama
# info: u fajlu postoje veverice u samo 3 boje
# kolona u kojoj je podatak o boji je "Primary Fur Color" - mogu biti Gray, Cinnamon i Black

data = pandas.read_csv("Squirrel_Data.csv")

color_count = data["Primary Fur Color"].value_counts()
df_1 = pandas.DataFrame(columns=["color", "count"])

for key in color_count.to_dict().keys():
    df_1.loc[len(df_1)] = [key, color_count.to_dict()[key]]

df_1.to_csv("new_data_1.csv", index=False)


grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict_2 = {
    "color": ["Gray", "Black", "Cinnamon"],
    "count": [grey_squirrels_count, black_squirrels_count, cinnamon_squirrels_count],
}
df_2 = pandas.DataFrame(data_dict_2)
df_2.to_csv("new_data_2.csv", index=False)















