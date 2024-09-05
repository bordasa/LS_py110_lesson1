import random, os

PLAY = True

PLAYER_MARKER = "X"
COMPUTER_MARKER = "O"
EMPTY_MARKER = " "
NUM_TO_WIN = 3 # In case I want to add the functionality for a bigger board

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

def display_game_screen(board_dict, player_score = 0, computer_score = 0):
    clear_screen()
    title_art()
    print(f"Player Marker: {PLAYER_MARKER} / Computer Marker: {COMPUTER_MARKER}")
    display_score(player_score, computer_score)
    #print(f"Computer Marker: {COMPUTER_MARKER}")
    # print(f"Computer Score: {computer_score}")
    display_board(board_dict)

def display_score(player_score, computer_score):
    print(f"Player Score: {player_score} / Computer Score: {computer_score}")

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
    comp_choice = None

    if board_dict[5] == EMPTY_MARKER:
        comp_choice = 5
    
    elif did_someone_win(board_dict, PLAYER_MARKER, 2)[0] == PLAYER_MARKER:
        for sublist in did_someone_win(board_dict, PLAYER_MARKER, 2)[1]:
            for square in sublist:
                if board_dict[square] is EMPTY_MARKER:
                    comp_choice = square
    
    if did_someone_win(board_dict, COMPUTER_MARKER, 2)[0] == COMPUTER_MARKER:
        for sublist in did_someone_win(board_dict, COMPUTER_MARKER, 2)[1]:
            for square in sublist:
                if board_dict[square] is EMPTY_MARKER:
                    comp_choice = square

    if comp_choice is None:
        comp_choice = random.choice(find_empty_squares(board_dict))

    board_dict[comp_choice] = COMPUTER_MARKER

def is_board_full(board_dict):
    return len(find_empty_squares(board_dict)) == 0

def did_someone_win(board_dict, marker, num_in_row):
    winning_options = [
                        (1, 2, 3), (4, 5, 6), (7, 8, 9),
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),
                        (1, 5, 9), (3, 5, 7)]

    winner = None
    winning_lines = []

    for sublist in winning_options:
        tracker = 0
        for square in sublist:
            if board_dict[square] == marker:
                tracker += 1
            
            if tracker == num_in_row:
                winner = marker
                winning_lines.append(sublist)
    
    return (winner, winning_lines)

def how_many_wins():
    while True:
        clear_screen()
        title_art()
        print()

        print("How many wins do you want to play to?")
        wins = input()

        if wins.isnumeric():
            return int(wins)
        
        else:
            print("Invalid input. Please enter an integer number.")

def who_goes_first():
    while True:
        clear_screen()
        title_art()
        print()

        print("Who will go first?")
        print("- 1: Player")
        print("- 2: Computer")
        who_first = input()

        if who_first == '1':
            return "player"
        
        elif who_first == '2':
            return "computer"
        
        else:
            print("Invalid input. Please type '1' or '2'.")

def switch_turns(who_just_went):
    if who_just_went == "player":
        return "computer"
    else:
        return "player"

while PLAY == True:
    player_score = 0
    computer_score = 0

    GAMES_TO_WIN = how_many_wins()

    current_turn = who_goes_first()

    while True:
        board_dict = create_fresh_board()
        GAME_END = False

        if player_score == GAMES_TO_WIN or computer_score == GAMES_TO_WIN:
            break

        while GAME_END == False:

            display_game_screen(board_dict, player_score, computer_score)

            if current_turn == "player":
                player_turn(board_dict)
            
            else:
                computer_turn(board_dict)

            display_game_screen(board_dict, player_score, computer_score)

            if did_someone_win(board_dict, PLAYER_MARKER, NUM_TO_WIN)[0] == PLAYER_MARKER:
                input("You win!")
                player_score += 1
                GAME_END = True
                break

            if did_someone_win(board_dict, COMPUTER_MARKER, NUM_TO_WIN)[0] == COMPUTER_MARKER:
                input("Computer wins!")
                computer_score += 1
                GAME_END = True
                break

            if is_board_full(board_dict):
                input("This game is a Tie!")
                GAME_END = True
                break

            current_turn = switch_turns(current_turn)
        
    while True:
        clear_screen()
        title_art()
        print()
        display_score(player_score, computer_score)
        print()

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