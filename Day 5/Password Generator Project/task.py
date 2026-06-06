# zadatak je da se kreira password od random karaktera. Korisnik odredjuje koliko  zeli slova, koliko brojeva i koliko specijalnih karaktera
# slova, brojevi i karakteri se random uzimaju iz listi a onda se random redjaju u password
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
letters_list  = []
numbers_list  = []
symbols_list  = []
password_length = nr_letters + nr_symbols + nr_numbers

for t in range(0, nr_letters):
    letters_list.append(letters[random.randint(0, len(letters) - 1)])

for t in range(0, nr_numbers):
    numbers_list.append(numbers[random.randint(0, len(numbers) - 1)])

for t in range(0, nr_symbols):
    symbols_list.append(symbols[random.randint(0, len(symbols) - 1)])

all_list = [letters_list, symbols_list, numbers_list]
print(all_list)

# dok je duzina password-a manja od zeljene while petlja ce se vrteti
# posto su elementi u liste letters_list, symbols_list i numbers_list dodati sa random onda moze da se uzima uvek prvi element iz liste sa pop(0)
while len(password) < password_length:
    # da bi u passwod bila izmesan sloba, brojevi i simpoli sa random se odlucuje iz koje ce se liste uzeti element za password
    l = random.randint(0, len(all_list)-1)
    if len(all_list[l]) > 0:
        #print(f"all_list[e].pop(0): {all_list[e].pop(0)}")
        password += all_list[l].pop(0)

print(f"final password: {password}")
