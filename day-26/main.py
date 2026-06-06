import random

numbers = [1, 2, 3]
# new_list = [(n + 1) for n in numbers]
new_list = [(f"{n} je paran broj") if n%2 == 0 else (f"{n} je neparan broj") for n in numbers]

print(new_list)

########################### List Comprehension ###########################
numbers = [n*2 for n in range(1, 5)]
print(numbers)

even_numbers = [n for n in range(1, 10) if n%2 == 0]
print(even_numbers)


########################### Dictionary Comprehension ###########################
# old_dict je pocetni dictionary
# {} - sa ovime kreiramo dictionary
# item - jedan element u old_dict
# new_key:new_value - sa ovime se uzimaju vrednosti iz old_dict
# new_dict = {new_key:new_value for item in old_dict}

# ovako se koristi
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# moze da se koristi i uslov
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# loop kroz listu i kreiranje dictionary
# dodaje se random score za svako ime iz liste i kreira se dictionary
names = ["Pera", "Mika", "Zika", "Tika", "Moca", "Peca"]

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores) # {'Pera': 67, 'Mika': 4, 'Zika': 79, 'Tika': 93, 'Moca': 52, 'Peca': 7}


# loop kroz dict i kreiranje novog dictionary
# kreira se novi dict koji ce sadrzati samo studente koji su polozili tj. imaju score >= 60
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students) # {'Pera': 67, 'Zika': 79, 'Tika': 93}




sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split(" ")
result = {word: len(word) for word in sentence_list}
print(result) # {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula: (temp_c * 9/5) + 32 = temp_f
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((temp * 9/5) + 32) for day, temp in weather_c.items()}
print(weather_f) # {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}


############################### iteracija kroz Pandas DataFrame ###############################
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# iteracija kroz dictionary sa for petljom
for (key, value) in student_dict.items():
    print(key)
    print(value)

# na DataFrame mozemo d agledamo kao na dictionary pa se na isti nacin i iterira kroz DataFrame
# importuje se pandas da bi se od dict kreirao DataFrame
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)

# pandas ima svoju metodu za iteraciju kroz podatke (redove) i to je iterrows()
# ova metoda vraca index reda i red sa svim podacima (i imenima kolona) u tom redu
# svaki red je serija pandas objekata. Iz tih objekata podatak se uzima sa row.ime_kolone
for (index, row) in student_data_frame.iterrows():
    print(f"{row.student}: {row.score}")
# Angela: 56
# James: 76
# Lily: 98








































