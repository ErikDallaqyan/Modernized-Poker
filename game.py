from Card_Submission import Submission
from Computer_actions import CA

Chips_amount = 3750
Computer_chips_amount = 3750
Bet = 0
separator = "***"

def get_minimum_bid():
    while True:
        try:
            minimum_bid = int(input("Please enter the minimum bid (50/100/250/500): "))
            if minimum_bid in [50, 100, 250, 500]:
                return minimum_bid
            else:
                print("Invalid bid amount. Please enter 50, 100, 250, or 500.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_action_choice():
    while True:
        action = input("Enter your action, for Fold is 'f', for Call/Check is 'c', for Raise is 'r': ").lower()
        if action in ['f', 'c', 'r']:
            return action
        else:
            print("Invalid action. Please enter 'f', 'c', or 'r'.")

def calculate_combination(cards):
    comb_dict = {}
    for num in cards:
        if str(num) in comb_dict:
            comb_dict[str(num)] += 1
        else:
            comb_dict[str(num)] = 1
    return comb_dict

def determine_winner(player_comb_dict, computer_comb_dict):
    if (3 in player_comb_dict.values() and 2 in player_comb_dict.values()) and not (3 in computer_comb_dict.values() and 2 in computer_comb_dict.values()):
        return "Full House"
    elif 4 in player_comb_dict.values() and 4 not in computer_comb_dict.values():
        return "Four of a Kind"
    elif 3 in player_comb_dict.values() and 4 not in computer_comb_dict.values() and 3 not in computer_comb_dict.values():
        return "Three of a Kind"
    elif 2 in player_comb_dict.values() and 4 not in computer_comb_dict.values() and 3 not in computer_comb_dict.values() and 2 not in computer_comb_dict.values():
        return "Pair"
    else:
        return "High Card"

for i in range(10):
    minimum_bid = get_minimum_bid()
    print(separator)
    Submission.YCI(Submission.y)
    
    Chips_amount -= minimum_bid
    Computer_chips_amount -= minimum_bid
    Bet += (minimum_bid * 2)
    
    print(f"The bet is: {Bet}")
    print(f"Your chips amount now: {Chips_amount}")
    
    Action_choice = get_action_choice()
    
    if Action_choice == "f":
        print(f"You lost. Your chips amount is: {Chips_amount}")
        Computer_chips_amount += Bet
        Bet = 0
        print(f"Computer chips amount now is: {Computer_chips_amount}")
    elif Action_choice == 'c':
        print(separator)
        
        CA.computer_action(CA.x)
        CA.cards_opening(CA.first_card, CA.second_card, CA.third_card, CA.fourth_card, CA.fifth_card)
        
        Action_choice_2 = get_action_choice()
        
        if Action_choice_2 == "f":
            print(separator)
            print(f"You lost. Your chips amount is: {Chips_amount}")
            Computer_chips_amount += Bet
            Bet = 0
            print(f"Computer chips amount now is: {Computer_chips_amount}")
        elif Action_choice_2 == "c":
            player_comb_list = [CA.splited_player_cards_1[0], CA.splited_player_cards_2[0], 
                                CA.splited_first_card[0], CA.splited_second_card[0], 
                                CA.splited_third_card[0], CA.splited_fourth_card[0], 
                                CA.splited_fifth_card[0]]
            
            computer_comb_list = [CA.splited_computer_cards_1[0], CA.splited_computer_cards_2[0], 
                                  CA.splited_first_card[0], CA.splited_second_card[0], 
                                  CA.splited_third_card[0], CA.splited_fourth_card[0], 
                                  CA.splited_fifth_card[0]]
            
            player_comb_dict = calculate_combination(player_comb_list)
            computer_comb_dict = calculate_combination(computer_comb_list)
            
            result = determine_winner(player_comb_dict, computer_comb_dict)
            
            if result != "High Card":
                print(f"You Won! Your combination is '{result}'")
                Chips_amount += Bet
                Bet = 0
                print(f"Your chips amount is now {Chips_amount}")
            else:
                high_card_list = [CA.splited_computer_cards_1[0], CA.splited_computer_cards_2[0], 
                                  CA.splited_player_cards_1[0], CA.splited_player_cards_2[0]]
                if max(high_card_list) in [CA.splited_player_cards_1[0], CA.splited_player_cards_2[0]]:
                    print("You Won! Your combination is 'High Card'")
                    Chips_amount += Bet
                    Bet = 0
                    print(f"Your chips amount is now {Chips_amount}")
                else:
                    print("You Lost!")
                    Computer_chips_amount += Bet
                    Bet = 0
                    print(f"Your chips amount is now {Chips_amount}")
        elif Action_choice_2 == "r":
            while True:
                try:
                    raise_amount = int(input(f"How much do you want to raise? (0-{Chips_amount}): "))
                    if 0 <= raise_amount <= Chips_amount:
                        break
                    else:
                        print(f"Invalid raise amount. Please enter a number between 0 and {Chips_amount}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            print(separator)
            Bet += (raise_amount*2)
            
            player_comb_list = [CA.splited_player_cards_1[0], CA.splited_player_cards_2[0], 
                                CA.splited_first_card[0], CA.splited_second_card[0], 
                                CA.splited_third_card[0], CA.splited_fourth_card[0], 
                                CA.splited_fifth_card[0]]
            
            computer_comb_list = [CA.splited_computer_cards_1[0], CA.splited_computer_cards_2[0], 
                                  CA.splited_first_card[0], CA.splited_second_card[0], 
                                  CA.splited_third_card[0], CA.splited_fourth_card[0], 
                                  CA.splited_fifth_card[0]]
            
            player_comb_dict = calculate_combination(player_comb_list)
            computer_comb_dict = calculate_combination(computer_comb_list)
            
            result = determine_winner(player_comb_dict, computer_comb_dict)
            
            if result != "High Card":
                print(f"You Won! Your combination is '{result}'")
                Chips_amount += Bet
                Bet = 0
                print(f"Your chips amount is now {Chips_amount}")
            else:
                high_card_list = [CA.splited_computer_cards_1[0], CA.splited_computer_cards_2[0], 
                                  CA.splited_player_cards_1[0], CA.splited_player_cards_2[0]]
                if max(high_card_list) in [CA.splited_player_cards_1[0], CA.splited_player_cards_2[0]]:
                    print("You Won! Your combination is 'High Card'")
                    Chips_amount += Bet
                    Bet = 0
                    print(f"Your chips amount is now {Chips_amount}")
                else:
                    print("You Lost!")
                    Computer_chips_amount += Bet
                    Bet = 0
                    print(f"Your chips amount is now {Chips_amount}")
        while True:
            try:
                raise_amount = int(input(f"How much do you want to raise? (0-{Chips_amount}): "))
                if 0 <= raise_amount <= Chips_amount:
                    break
                else:
                    print(f"Invalid raise amount. Please enter a number between 0 and {Chips_amount}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            

    elif Action_choice == 'r':
        print(separator)
        while True:
            try:
                raise_amount = int(input(f"How much do you want to raise? (0-{Chips_amount}): "))
                if 0 <= raise_amount <= Chips_amount:
                    break
                else:
                    print(f"Invalid raise amount. Please enter a number between 0 and {Chips_amount}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        Bet += raise_amount
        print(f"The bet is: {Bet}")
        print("Computer calls")
        Computer_chips_amount -= raise_amount
        Bet += raise_amount
        CA.computer_action(CA.x)
        CA.cards_opening(CA.first_card, CA.second_card, CA.third_card, CA.fourth_card, CA.fifth_card)
    
    if Chips_amount <= 0:
        print("You lost!")
        break
    if Computer_chips_amount <= 0:
        print("Congratulations, you won this game!")
        break
