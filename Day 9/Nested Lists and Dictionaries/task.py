capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": {"Berlin", "Hamburg"},
}

print(travel_log["France"][1])

print("******************************************")

for t, v in travel_log.items():
    for i in v:
        print(i)


cities = {"Berlin", "Hamburg"}