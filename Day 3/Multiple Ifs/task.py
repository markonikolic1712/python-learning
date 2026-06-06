print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    #elif age >= 45 and age <= 55:
    elif 45 >= age <= 55:
        print("Free ride 😲 => tickets are $0.")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Would you like to see the picture of you? (y/n)")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
