import random, os

PLAY = True
GAME_END = False
ROWS = 3
COLUMNS = 3
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'

def title_art():
    print("=======================")
    print("===   TIC TAC TOE   ===")
    print("=======================")

def clear_screen():
    os.system('cls||clear')

def make_board_dict(rows, columns):
    board_dict = {}

    for row in range(rows):
        row_list = []
        for col in range(columns):
            row_list.append([" "])

        board_dict[row] = row_list

    return board_dict

def display_board(board_dict):
    title_art()
    print(f"You are {PLAYER_MARKER}. Computer is {COMPUTER_MARKER}.")
    print()

    top_row = " "
    for col in range(COLUMNS):
        top_row += f"   {col}   "
        
    print(top_row)

    for row in board_dict.keys():
        print(f"{row}{board_dict[row]}")
    
    print()

def player_turn_input(board_dict):
    VALID_INPUT = False
    while not VALID_INPUT:
        print("Where would you like to mark the board?")
        print("Input your answer as Row then Column")
        player_input = input("Example: 12 for Row 1 Column 2\n")

        if player_input and player_input[0].isnumeric():
            if int(player_input[0]) in range(ROWS):
                row_input = int(player_input[0])
            
                for char in player_input[1:]:
                    if char.isnumeric() and int(char) in range(COLUMNS):
                        column_input = int(char)
            
                    if board_dict[row_input][column_input] == [' ']:
                        VALID_INPUT = True
                    else:
                        print("Invalid input.")
                        input("That space is taken, please try again.")
        
        else:
            print("Invalid input.")
            input("Please input a square in the format of ROW COLUMN.")
    
    board_dict[row_input][column_input] = ["X"]
    player_turns_list.add((row_input, column_input))

def computer_turn(board_dict):
    open_spaces = []

    for row, row_list in board_dict.items():
        for col in range(len(row_list)):
            if ' ' in board_dict[row][col]:
                open_spaces.append((row, col))

    row_choice, column_choice = random.choice(open_spaces)

    board_dict[row_choice][column_choice] = ["O"]
    computer_turns_list.add((row_choice, column_choice))

def did_someone_win(turn_list):
    winning_options = [{(0, 0), (0, 1), (0, 2)},
                       {(1, 0), (1, 1), (1, 2)},
                       {(2, 0), (2, 1), (2, 2)},
                       {(0, 0), (1, 0), (2, 0)},
                       {(0, 1), (1, 1), (2, 1)},
                       {(0, 2), (1, 2), (2, 2)},
                       {(0, 0), (1, 1), (2, 2)},
                       {(0, 2), (1, 1), (2, 0)}]
    
    for sublist in winning_options:
        if sublist.issubset(turn_list):
            return True
    return False

def is_board_full(turn_list1, turn_list2):
    if len(turn_list1) + len(turn_list2) == ROWS * COLUMNS:
        return True
    else:
        return False
####
####################################################
####################################################

while PLAY == True:
    game_board_dict = make_board_dict(ROWS, COLUMNS)
    player_turns_list = set()
    computer_turns_list = set()

    while GAME_END == False:
        clear_screen()

        display_board(game_board_dict)
        
        player_turn_input(game_board_dict)

        clear_screen()

        display_board(game_board_dict)

        if did_someone_win(player_turns_list):
            print('Player wins!')
            GAME_END = True
            break

        elif is_board_full(player_turns_list, computer_turns_list):
            print("It's a tie!")
            GAME_END = True
            break

        computer_turn(game_board_dict)

        clear_screen()

        display_board(game_board_dict)

        if did_someone_win(computer_turns_list):
            print('Computer wins!')
            GAME_END = True
            break
        
    play_again = input("Would you like to play again?\n")
    if play_again[0].casefold() == "y":
        GAME_END = False
    else:
        input("Thank you for playing!\nPress Enter to close the game.")
        PLAY = False