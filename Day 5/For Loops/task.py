fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

print(fruits)

for index, fruit in enumerate(fruits, start=10):
    print(f"index: {index}; fruit: {fruit}")