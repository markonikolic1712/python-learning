
# range() se koristi u for loop petlji i nju koristiomo da u for petlji imamo zeljeni broj iteracija
# range(1, 10) ce iterirati 9 puta i dace na vrednosti od 1 do 9. Vrednost koju nam da mozemo da iskoristimo da iz liste uzmemo element po indeksu
# kada se koristi range() korak je po defaultu 1 a ako zelimo da bude drugaciji onda se on definise kao treci parametar
# range(1, 100, 3) ovde cemo imati iteraciju od 1 do 99 sa koracima od 3: 1, 4, 7, 10...


# ovo ce iterirati od 1 do 100 (ukljucujuci i 100) i kreirace sumu brojeva od 1 do 100
# total = 1+2+3+4+.....+97+98+99+100 = 5050
total = 0
for i in range(1, 101):
    total += i
print(total)

# ovo isto kreira sumu brojeva od 1 do 100 ali u duplo manje iteracija
# ako uzmemo listu od 1 do 100 i podelimo je na pola i obrnemo redosled druge polovine imamo
# 1   2   3   4   5 ...
# 100 99  98  97  96...
# sabiraju se 1 i 100, pa 2 i 99 i tako iamamo 50 parova/iteracija
total = 0
for i in range(1, 51):
    total += i + (101 - i)
print(total)


for i in range(1, 101):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

