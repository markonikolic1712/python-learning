import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_list = []
placeholder_list = []
lives = 6
tries = 0
win = False
placeholder = ""

for l in chosen_word:
    chosen_word_list.append(l)
    placeholder_list.append("_")

for i in range(len(chosen_word_list)+50):
    placeholder += placeholder_list[i]

print(chosen_word)
print(placeholder)

while lives > 0 and not win:
    guess_letter = input("Guess a letter: ").lower()
    letter_correct = False

    for i in range(len(chosen_word_list)):
        if guess_letter == chosen_word_list[i]:
            placeholder_list[i] = guess_letter
            letter_correct = True

    if not letter_correct:
        lives -= 1
        print("Wrong guess!")
        print(stages[lives])

    placeholder = ""
    for p in placeholder_list:
        placeholder += p

    if placeholder == chosen_word:
        win = True

    print(f"placeholder: {placeholder}; lives: {lives}/6")

print("GAME OVER! " + ("YOU WIN" if win else "YOU LOSE"))