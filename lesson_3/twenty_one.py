import random, os

def clear_screen():
    os.system('cls||clear')

def join_or(item_list, delimiter = ', ', connector = 'or'):

    item_list = [str(item) for item in item_list]

    if len(item_list) == 0:
        return ""
    elif len(item_list) == 1:
        return item_list[0]
    elif len(item_list) == 2:
        return f"{item_list[0]} {connector} {item_list[1]}"
    else:
        return f"{delimiter}".join(item_list[:-1]) + f"{delimiter}{connector} {item_list[-1]}"

def build_deck():
    card_values_dict = {'two': 2, 'three': 3, 'four': 4,
                        'five': 5, 'six': 6, 'seven': 7,
                        'eight': 8, 'nine': 9, 'ten': 10,
                        'jack': 10, 'queen': 10, 'king': 10,
                        'ace': 11,
                        }
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    deck = []
    
    for name, value in card_values_dict.items():
        for suit in suits:
            deck.append((name, value, suit))
    
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]

    return player_cards, dealer_cards

def show_dealer_faceup_card(d_hand):
    print(f"Dealer has: {d_hand[0][0].capitalize()} of {d_hand[0][2].capitalize()}.")
    print()

def declare_player_cards(p_hand):
    total = calc_total(p_hand)

    card_names = [card[0].capitalize() for card in p_hand]
    
    print(f"You have: {join_or(card_names, ', ', 'and')}.")
    print(f"Your current total is {total}.")
    print()

def declare_dealer_cards(d_hand):
    total = calc_total(d_hand)

    card_names = [card[0].capitalize() for card in d_hand]
    
    print(f"Dealer has: {join_or(card_names, ', ', 'and')}.")
    print(f"Dealer's total is {total}.")
    print()

# def display_card(card):

#     if card[1] == 10:
#         if card[0] == 'ten':
#             card_num = 10
#         else:
#             card_num = card[0][0].upper()
#     else:
#         card_num = card[1]

#     print(".--------.")

#     if card_num == 10:
#         print(f"|{card_num}.--.  |")
#     else:
#         print(f"|{card_num} .--.  |")

#     match card[2]:
#         case 'diamonds':
#             print("|  :/\:  |")
#             print("|  :\/:  |")
        
#         case 'hearts':
#             print("|  (\/)  |")
#             print("|  :\/:  |")

#         case 'clubs':
#             print("|  :():  |")
#             print("|  ()()  |")
        
#         case 'spades':
#             print("|  :/\:  |")
#             print("|  (__)  |")

#     if card_num == 10:
#         print(f"|  '--'{card_num}|")
    
#     else:
#         print(f"|  '--' {card_num}|")

#     print(f"`--------'")

def calc_total(p_hand):
    cards = [card[0] for card in p_hand]
    aces = cards.count('ace')
    total = sum([card[1] for card in p_hand])

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def player_turn(p_hand, deck):

    while True:
        clear_screen()
        current_total = calc_total(p_hand)

        declare_player_cards(p_hand)

        while current_total < 21:
            print("What will you do?")
            print("-1. Hit")
            print("-2. Stay")
            player_decision = input()

            if player_decision == '1':
                # clear_screen()
                print("You chose to Hit.")
                p_hand.append(deck.pop())

                current_total = calc_total(p_hand)
                declare_player_cards(p_hand)
            
            elif player_decision == '2':
                print("You chose to stay!")
                input()
                return p_hand, current_total
            
            else:
                print("Invalid option. Please input 1 or 2.")

        if current_total == 21:
            print("You have 21!")
            input()
            return p_hand, current_total
        
        else:
            print("You have busted!")
            input()
            return p_hand, current_total
    
def dealer_turn(d_hand, deck):
    dealer_total = calc_total(d_hand)
    declare_dealer_cards(d_hand)

    while dealer_total < 17:
        clear_screen()
        print("Dealer hits.")
        d_hand.append(deck.pop())
        dealer_total = calc_total(d_hand)
        declare_dealer_cards(d_hand)

    if dealer_total == 21:
        print("Dealer has 21")
        input()
    
    elif dealer_total < 21:
        print("Dealer stays.")
        input()
    
    else:
        print("Dealer has busted!")
        input()
    
    return d_hand, dealer_total

def declare_winner(player_total, dealer_total):
    if dealer_total > 21 or player_total > dealer_total:
        print("You win!")
    
    else:
        print("Dealer wins!")

###
clear_screen()
deck = build_deck()

shuffle(deck)

player_cards, dealer_cards = deal_cards(deck)

show_dealer_faceup_card(dealer_cards)

player_cards, player_total = player_turn(player_cards, deck)

if player_total >= 21:
    print("Dealer wins.")

else:
    dealer_cards, dealer_total = dealer_turn(dealer_cards, deck)

    declare_winner(player_total, dealer_total)
