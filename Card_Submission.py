import random

class Submission:

    Suits = ['Club', 'Diamond', 'Heart', 'Spade']
    Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 
    Card_list = []
    for rank in Ranks:
        for suit in Suits:
            Card_list.append(f'{rank} of {suit}')
    Given_cards_computer = []
    Given_cards_player = []

    for i in range(2):
        Given_card_player = random.choice(Card_list)
        Given_cards_player.append(Given_card_player)
        Card_list.remove(Given_card_player)

    for j in range(2):
        Given_card_computer = random.choice(Card_list)
        Given_cards_computer.append(Given_card_computer)
        Card_list.remove(Given_card_computer)   

    y = Given_cards_player
    def YCI(y):
        return f"Your card is: {y}"
    print(YCI(y))