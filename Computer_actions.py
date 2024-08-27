import random
from Card_Submission import Submission
import re 

class CA:
    x = Submission.Given_card_computer
    def computer_action(x):
        return "Computer checks cards"

    first_card = random.choice(Submission.Card_list)
    Submission.Card_list.remove(first_card)
    second_card = random.choice(Submission.Card_list)
    Submission.Card_list.remove(second_card)
    third_card = random.choice(Submission.Card_list)
    Submission.Card_list.remove(third_card)
    fourth_card = random.choice(Submission.Card_list)
    Submission.Card_list.remove(fourth_card)
    fifth_card = random.choice(Submission.Card_list)
    Submission.Card_list.remove(fifth_card)

    def cards_opening(first_card, second_card, third_card, fourth_card, fifth_card):
        print(f"First oppened card is: {first_card}")
        print(f"Second oppened card is: {second_card}")
        print(f"Third oppened card is: {third_card}")
        print(f"Fourth oppened card is: {fourth_card}")
        print(f"Fifth oppened card is: {fifth_card}")
        return " "

    print(computer_action(Submission.Given_cards_computer))
    print(cards_opening(first_card, second_card, third_card, fourth_card, fifth_card))



    splited_computer_cards_1 = re.findall("\w+", Submission.Given_cards_computer[0])
    splited_computer_cards_2 = re.findall("\w+", Submission.Given_cards_computer[1])
    splited_player_cards_1 = re.findall("\w+", Submission.Given_cards_player[0])
    splited_player_cards_2 = re.findall("\w+", Submission.Given_cards_player[1])
    splited_first_card = re.findall("\w+", first_card)
    splited_second_card = re.findall("\w+", second_card)
    splited_third_card = re.findall("\w+", third_card)
    splited_fourth_card = re.findall("\w+", fourth_card)
    splited_fifth_card = re.findall("\w+", fifth_card)