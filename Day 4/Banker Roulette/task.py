import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[random.randint(0, len(friends)-1)]) # uzimanje random elementa iz niza
# za uzimanje random elementa iz sekvenca moze da se koristi random funkcija choice() kojoj se prosledjuje lista
print(random.choice(friends))

