import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    card = random.choice(cards)
    return card
    
# Creating two empty lists.
user_cards = []
computers_cards = []

# This is a for loop that runs twice. The first time it runs, it appends a random card to the
# user_cards list and a random card to the computers_cards list. The second time it runs, it appends
# another random card to the user_cards list and another random card to the computers_cards list.
for _ in range(2):
    user_cards.append(deal_card())
    computers_cards.append(deal_card())
    
def calculate_score(cards):
    """
    If the sum of the cards is 21 and there are only two cards, return 0. 
    If there is an 11 in the cards and the sum of the cards is greater than 21, 
    remove the 11 and add a 1. 
    Finally, return the sum of the cards.
    
    :param cards: a list of integers representing the cards in the player's hand
    :return: The sum of the cards in the list.
    """
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """
    If the user and computer have the same score, it's a draw. If the user has a score of 0, they win
    with a blackjack. If the computer has a score of 0, they lose with a blackjack. If the user has a
    score over 21, they lose. If the computer has a score over 21, they win. If the user has a higher
    score than the computer, they win. Otherwise, they lose
    
    :param user_score: The user's score
    :param computer_score: The score of the computer's hand
    :return: The result of the game.
    """
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def play_game():
    """
    The function plays a game of blackjack, and prints the result of the game
    :return: the string that is returned by the compare function.
    """
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computers_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computers_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        print(compare(user_score, computer_score))
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        while user_should_deal == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"   Your cards: {user_cards}, current score: {user_score}")
            print(f"   Computer's first card: {computers_cards[0]}")
            if user_score > 21:
                print(compare(user_score, computer_score))
                return
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        
        while computer_score != 0 and computer_score < 17:
            computers_cards.append(deal_card())
            computer_score = calculate_score(computers_cards)
        
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computers_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))    
        
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
    
            
    