import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if player_choice >= 3:
        print("Please choose 1, 2 or 3.")
        continue

    choices = [rock, paper, scissors]

    computer_choice = random.randint(0, 2)

    print(f"You choose:\n{choices[player_choice]}\n")
    print(f"Computer choose:\n{choices[computer_choice]}\n")

    results = ["It's a draw!", "You win!", "Computer wins!"]
    result = 0
    if (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (
            player_choice == 2 and computer_choice == 0):
        result = 2
    elif (computer_choice == 0 and player_choice == 1) or (computer_choice == 1 and player_choice == 2) or (
            computer_choice == 2 and player_choice == 0):
        result = 1

    print(results[result])