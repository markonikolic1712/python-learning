import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# iterira se kroz DataFrame i kreira se dictionary u formatu: {"A": "Alfa", "B": "Bravo"}
alphabet = {row.letter:row.code for index, row in data.iterrows()}

# {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}
print(alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Please enter your name: ").upper()

name_alphabet = [alphabet[letter] for letter in name]
# Marko => ['Mike', 'Alfa', 'Romeo', 'Kilo', 'Oscar']
print(name_alphabet)

