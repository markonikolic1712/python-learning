def greet(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice?")

greet("Pera")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Positional arguments
# greet_with("Jack Bauer", "Nowhere")
# greet_with("Nowhere", "Jack Bauer")

# Keyword arguments
greet_with(location="London", name="Angela")
greet_with(name="Angela", location="London")