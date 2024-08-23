import random

ROWS = 3
COLUMNS = 3

def make_ttt_board_dict(rows, columns):
    board_dict = {}

    for row in range(rows):
        row_list = []
        for col in range(columns):
            row_list.append([" "])

        board_dict[row] = row_list

    return board_dict

def print_board(board_dict):
    
    top_row = " "
    for col in range(COLUMNS):
        top_row += f"   {col}   "
        
    print(top_row)

    for row in board_dict.keys():
        print(f"{row}{board_dict[row]}")

def collect_player_turn_input():
    while True:
        print("Where would you like to mark the board?\n")
        print("Input your answer as Row then Column\n")
        player_input = input("Example: 12 for R1 C2\n")

        if player_input[0] in range(ROWS):
            row_input = player_input[0]
            
            for char in  player_input[1:]:
                if char in range(COLUMNS):
                    column_input = char
                    break
    
    return (row_input, column_input)

def computer_turn(board_dict):
    open_spaces = []

    for row, row_list in board_dict.items():
        for col in range(len(row_list)):
            if ' ' in board_dict[row][col]:
                open_spaces.append((row, col))

    row_choice, column_choice = random.choice(open_spaces)

    update_board(board_dict, row_choice, column_choice, player = False)

def update_board(board_dict, row_input, column_input, player):
    if player:
        board_dict[row_input][column_input] = ["X"]
    else:
        board_dict[row_input][column_input] = ["O"]

game_board_dict = make_ttt_board_dict(ROWS, COLUMNS)

print_board(game_board_dict)

computer_turn(game_board_dict)

print_board(game_board_dict)