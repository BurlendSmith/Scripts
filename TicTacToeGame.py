# Imported libraries

import random

#############################################################################################################################################

#Prints a board

game_on = True

def display_board(board):
    print(" " + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("-----------")
    print(" " + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("-----------")
    print(" " + board[1] + ' | ' + board[2] + ' | ' + board[3])

#############################################################################################################################################

#Takes in player input

def player_input():

    marker = ''

    # KEEP ASKING PLAYER 1 TO CHOOSE X OR O

    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose 'X' or 'O'?: \n").upper()
        if marker != 'X' and marker != 'O':
            print("Sorry, your choice is not 'X' or 'O' \n")

    # ASSIGNS PLAYER 2 THE OPPOSITE MARKER

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f"Player 1: you're '{player1}'")
    print(f"Player 2: you're '{player2}'\n")
    ready_to_play = input("Are you ready to play? Enter Yes or No.\n").capitalize()
    if ready_to_play == 'Yes':
        print("Enjoy!\n")
        game_on = True
    else:
        exit()

    return (player1,player2)

#############################################################################################################################################

# Places player inputs on the board

def place_marker(board, marker, position):
    # ASSIGNS MARKER TO POSITION
    board[position] = marker

#############################################################################################################################################

#Check if the game is won,tied, lost, or ongoing.

def win_check(board, marker):
    return ((board[7] == board[8] == board[9] == marker) or     # Checks Rows
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            (board[7] == board[4] == board[1] == marker) or     # Checks Columns
            (board[8] == board[5] == board[2] == marker) or
            (board[9] == board[6] == board[3] == marker) or
            (board[7] == board[5] == board[3] == marker) or     # Checks Diagonals
            (board[9] == board[5] == board[1] == marker))

#############################################################################################################################################

# Choose who goes first.

def choose_first():

    global player1_guess
    global player2_guess
    player1_guess = 21
    player2_guess = 21
    correct_num = random.randint(1,10)

    print("I am thinking of a number in between 1 and 10.")
    print("The player that enters a number that's closest to the number I am thinking of goes first.\n")

    # Keeps asking players to input a number

    while player1_guess not in range(1,11):

        player1_guess = int(input("Player 1: Please enter a number (1-10): "))

        if player1_guess not in range(1,11):
            print("Sorry, your number isn't in the given range")
            continue

    while player2_guess not in range(1,11):

        player2_guess = int(input("Player 2: Please enter a number (1-10): "))

        if player2_guess not in range(1,11):
            print("Sorry, your number isn't in the given range.")
            continue

    # Determines which input value was closest to the randomly generated value

    if abs(player1_guess - correct_num) > abs(player2_guess - correct_num):
        turn = "Player 2"
        print(f"The number that I was thinking of was {correct_num}.\n")
        return turn
    else:
        turn = "Player 1"
        print(f"The number that I was thinking of was {correct_num}.\n")
        return turn
#############################################################################################################################################

# Asks for a player's next position

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position (1-9): "))
        if position not in range(1,10):
            print('Sorry, the entered value is invalid\n')

    return position

#############################################################################################################################################

# Checks if the selected space is available

def space_check(board, position):

    return board[position] == " "

#############################################################################################################################################

# Checks if the board is full or not

full_board = False

def full_board_check(board):
    count = 0
    for item in board:
        if item == 'X' or item == 'O':
            count += 1

    if count == 9:
        full_board = True
        game_on = False
        if full_board == True:
            print("The board is full.")

#############################################################################################################################################

# Asks player if they want to play again

def replay():
    replay_choice = input("Play again? Enter Yes or No").capitalize()
    if replay_choice == "Yes":
        game_on = True
        return replay_choice
    else:
        print("Thank you for playing!")
        exit()

#############################################################################################################################################

# Connects everything together

print("Welcome to Tic Tac Toe!\n")

while True:
    the_board = [" "] * 10
    turn = choose_first()
    print(turn + " will go first.\n")
    player1_marker,player2_marker = player_input()

    while game_on:

        if turn == "Player 1":
            # Shows board
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            # Checks if Player 1 won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 WINS!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            # Shows board
            display_board(the_board)
            #Choose position
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            # Checks if Player 2 won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 WINS!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break



# Current tasks:
# Figure out why place_marker function works but not the player choice fucntion
# Figure out how to alternate between player 1 and player 2 (Function?)
# Figure out to use x's and o's on board (Now it's only showing me player 1's marker)
# Make function that knows the difference between player1 and player2's marker
    # Doing this to see if it would actually add the marker to the board
    # if (some condition that knows its player1's turn), board[next_position]+= player1 (opposite for player2)








