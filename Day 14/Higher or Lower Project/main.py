import random
import art
import game_data

# Compare A: {name}, {description}, from {country}.
# Compare B: {name}, {description}, from {country}.
# Who has more followers? Type 'A' or 'B':
# You're right!. Current score: {score}.
# Sorry, that's wrong. Final score: {score}

# u igri korisnik pogadja koji instagram account ima vise pratilaca

def play_game():
    #print(art.logo)
    is_correct_answer = True
    score = 0
    data = game_data.data
    account_a_index = random.randint(0, len(data)-1)

    # u compare_a i compare_b ce biti objekti koji ce sadrzati podatke koji se porede
    account_a = data[account_a_index]
    account_b = None



    # dok igrac tacno odgovara igra se nastavlja
    # nakon svakog poredjenja objekat B prelazi u osobu A a za B se uzima novi objekat za poredjenje
    while is_correct_answer:
        print(art.logo)
        if not (account_b is None):
            print(f"You're right!. Current score: {score}.")

        account_b_index = random.randint(0, len(data) - 1)

        # ako se desi da su isti indeksi budu isti onda se za objekat B uzima novi indeks
        if account_b_index == account_a_index:
            continue

        account_b = data[account_b_index]

        print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
        print(art.vs)
        print(f"Compare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if not(answer == 'a' or answer == 'b'):
            print("Please enter 'A' or 'B'.")
            continue

        is_correct_answer, score, goes_to_next_round = check_answer(answer, account_a, account_b, score)

        # sada se objekat B setuje u objekat A
        account_a = goes_to_next_round


def check_answer(answer, account_a, account_b, score):
    is_correct_answer = True
    goes_to_next_round = {}
    if answer == 'a' and account_a['follower_count'] > account_b['follower_count']:
        score += 1
        goes_to_next_round = account_a
    elif answer == 'b' and account_b['follower_count'] > account_a['follower_count']:
        score += 1
        goes_to_next_round = account_b
    elif account_a['follower_count'] == account_b['follower_count']:
        print(f"They have the same number of followers.")
        print("Score is unchanged. Game continues.")
        goes_to_next_round = account_a
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_correct_answer = False

    return is_correct_answer, score, goes_to_next_round


play_game()