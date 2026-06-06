import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_to_play = 'y'

# "Lose, opponent has Blackjack 😱"
# "Win with a Blackjack 😎"
# "You went over. You lose 😭"
# "Opponent went over. You win 😁"
# "You win 😃"
# "You lose 😤"

# "Type 'y' to get another card, type 'n' to pass: "
# print(f"Your cards: {user_cards}, current score: {user_score}")
# print(f"Computer's first card: {computer_cards[0]}")


def deal_card():
    return random.choice(cards)

def calculate_score(cards_to_calculate):
    #if sum(cards_to_calculate) > 21 and 11 in cards_to_calculate:
    if sum(cards_to_calculate) > 21 and cards_to_calculate.__contains__(11):
        cards_to_calculate.remove(11)
        cards_to_calculate.append(1)
        return sum(cards_to_calculate)
    else:
        return sum(cards_to_calculate)

def compare_scores(user_cards, computer_cards):
    print("***************** FINAL RESULT *****************")
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif user_score == 21:
        return "Win with a Blackjack 😎"
    elif computer_score == 21:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == computer_score:
        return  "Draw!"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose!"


def play_game():
    user_cards = []
    computer_cards = []

    while len(user_cards) < 2:
        user_cards.append(deal_card())
    while len(computer_cards) < 2:
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 21:
        print("Win with a Blackjack 😎")
        return
    if computer_score == 21:
        print("Lose, opponent has Blackjack 😱")
        return

    is_game_over = False

    while not is_game_over:
        if not is_game_over and calculate_score(user_cards) < 21:
            new_card_for_user = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if new_card_for_user != "y": is_game_over = True
            if new_card_for_user == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
        else:
            is_game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare_scores(user_cards, computer_cards))

while want_to_play == "y":
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == "y":
        print("\n" * 20)
        print(art.logo)
        play_game()


