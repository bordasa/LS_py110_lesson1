import random, os

PLAY = True
GAME_END = False

PLAYER_MARKER = "X"
COMPUTER_MARKER = "O"
EMPTY_MARKER = " "
NUM_TO_WIN = 3

def title_art():
    print("===================================")
    print("=========   TIC TAC TOE   =========")
    print("===================================")

def clear_screen():
    os.system('cls||clear')

def display_board(board_dict):
    print()
    print("           |           |")
    print("           |           |")
    print(f"     {board_dict[1]}     |     {board_dict[2]}     |     {board_dict[3]}")
    print("           |           |")
    print("           |           |")
    print("-----------+-----------+-----------")
    print("           |           |")
    print("           |           |")
    print(f"     {board_dict[4]}     |     {board_dict[5]}     |     {board_dict[6]}")
    print("           |           |")
    print("           |           |")
    print("-----------+-----------+-----------")
    print("           |           |")
    print("           |           |")
    print(f"     {board_dict[7]}     |     {board_dict[8]}     |     {board_dict[9]}")
    print("           |           |")
    print("           |           |")
    print()

def display_game_screen(board_dict):
    clear_screen()
    title_art()
    print(f"Player Marker: {PLAYER_MARKER}")
    print(f"Computer Marker: {COMPUTER_MARKER}")
    display_board(board_dict)

def create_fresh_board():
    fresh_board_dict = {}

    for key in range(1, 10):
        fresh_board_dict[key] = EMPTY_MARKER
    
    return fresh_board_dict

def find_empty_squares(board_dict):
    empty_squares = []

    for key, value in board_dict.items():
        if value == EMPTY_MARKER:
            empty_squares.append(key)
    
    return empty_squares

def and_or_items(item_list, connector):

    item_list = [str(item) for item in item_list]

    if len(item_list) < 2:
        return item_list[0]
    else:
        return ", ".join(item_list[:-1]) + f" {connector} {item_list[-1]}"

def player_turn(board_dict):
    available_squares = find_empty_squares(board_dict)

    while True:
        print("Please select a square:")
        player_input = input(and_or_items(available_squares, 'or') + "\n")

        if player_input and int(player_input) in available_squares:
            break
        else:
            print("Invalid input")

    board_dict[int(player_input)] = PLAYER_MARKER

def computer_turn(board_dict):
    comp_choice = random.choice(find_empty_squares(board_dict))

    board_dict[comp_choice] = COMPUTER_MARKER


def is_board_full(board_dict):
    return len(find_empty_squares(board_dict)) == 0

def did_someone_win(board_dict, marker):
    winning_options = [
                        (1, 2, 3), (4, 5, 6), (7, 8, 9),
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),
                        (1, 5, 9), (3, 5, 7)]

    for sublist in winning_options:
        tracker = 0
        for square in sublist:
            if board_dict[square] == marker:
                tracker += 1
            
            if tracker == NUM_TO_WIN:
                return marker
    
    return None


while PLAY == True:
    board_dict = create_fresh_board()

    while GAME_END == False:

        display_game_screen(board_dict)

        player_turn(board_dict)

        display_game_screen(board_dict)

        if did_someone_win(board_dict, PLAYER_MARKER) == PLAYER_MARKER:
            print("You win!")
            GAME_END = True
            break

        if is_board_full(board_dict):
            print("This game is a Tie!")
            GAME_END = True
            break

        computer_turn(board_dict)

        display_game_screen(board_dict)

        if did_someone_win(board_dict, COMPUTER_MARKER) == COMPUTER_MARKER:
            print("Computer wins!")
            GAME_END = True
            break

        if is_board_full(board_dict):
            print("This game is a Tie!")
            GAME_END = True
            break
    
    while True:
        print("Would you like to play again? (yes/no)")
        play_again = input()

        if play_again:
            if play_again[0].casefold() == 'n':
                input("Thanks for playing. Press Enter to Quit.")
                PLAY = False
                break

            elif play_again[0].casefold() == 'y':
                GAME_END = False
                break
        
        else:
            print("Invalid input. Please type 'yes' or 'no'.")