import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    card = random.choice(cards)
    return card
    
user_cards = []
computers_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
        
    