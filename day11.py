import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10
             ]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """takes a list and calculate it retuing the sum"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score == computer_score :
        return "its a drawc😶"
    elif computer_score == 0 :
        return "you lose computer has a blackjack🤐"
    elif user_score == 0 :
        return "you win with a blackjack🎊"
    elif computer_score > 21 :
        return "computer went over u win🎊"
    elif user_score > 21 :
        return "you went over computer wins🤐"
    elif user_score > computer_score :
        return "you win 🎊"
    else:
        return"computer wins🤐"
def play_game():
    user_card = []
    computer_card = []
    is_game_over = True
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while  is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"{user_card} {user_score}")
        print(f"{computer_card[0]} ")
        if user_score == 0 or computer_score == 0 or user_score > 21 :
            is_game_over = False
        else:
            ask = input("do you another card typ y for yes and n for no: ")
            if ask == "y":
                user_card.append(deal_card())
            else:
                is_game_over = False

    while computer_score != 0 and computer_score < 17 :
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"your hand is {user_card} and final score is {user_score}")
    print(f"computer hand is {computer_card} and final score is {computer_score}")
    print(compare(user_score,computer_score))
while input(" do you want to play type y for yes and n for no ") == "y" :
        play_game()