states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia"]
states_of_america[2] = "BBBBBBBB" # promena vrednosti elementa u listi
states_of_america.sort(key=str.lower)
states_of_america[3] = "AAAAAAAA" # ako se element menja nakon sort() vrednost nece biti ukljucena u sortiranje. Ovo bi po sort() trebalo da bude na pocetku ali nece biti

states_of_america.append("XXXXXXXXXXXX") # dodavanje elementa na kraj liste
states_of_america.extend(["YYY", "ZZZ"]) # dodavanje vise elemenata na kraj liste

for i in states_of_america:
    print(f"{states_of_america.index(i)+1}. item: {i}")
    print()


