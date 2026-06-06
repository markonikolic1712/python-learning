programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

for k in programming_dictionary:
    print(k) # ovo vraca vrednost kljuca: Bug, Function, Loop
    print(programming_dictionary[k]) # ovo po kljucu uzima value

programming_dictionary.clear()
print(programming_dictionary)


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for s, g in student_scores.items():
    if g > 90:
        student_grades[s] = "Outstanding"
    elif g > 80:
        student_grades[s] = "Exceeds Expectations"
    elif g > 70:
        student_grades[s] = "Acceptable"
    else:
        student_grades[s] = "Fail"

for s, g in student_grades.items():
    print(f"{s} -> {g}")





