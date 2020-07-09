# NUMBER GUESSING GAME

import random

num = random.randint(1,20)

def give_clue():
	if num % 2 == 0 and num % 5 == 0:
		print('The number is even and divisible by 5.')
	elif num % 2 == 0:
		print('The number is even')
	elif num % 5 == 0:
		print('The number is divisible by 5')
	elif num % 5 != 0:
		print('The number is not divisible by 5')

	else:
		print('The number is odd.')

def you_win():
	print('CONGRATULATIONS YOU GUESSED CORRECTLY. \nI WAS THINKING OF {}'.format(num))
	game_on = False

def you_lose():
	print('SORRY YOU GUESSED CORRECTLY FOUR TIMES.\nYOU LOSE:( \nI WAS THINKING OF {}'.format(num))
	game_on = False

def replay():
	choice = input('PLAY AGAIN? ENTER Y/N ')
	if choice == 'Y'.upper():
		return True
	else:
		print('THANKS FOR PLAYING:)')
		print("PRESS 'ENTER' TO QUIT")

def reduced_score(score):
	score-=25
	if score == 0:
		you_lose()
	print('YOUR SCORE HAS BEEN REDUCED TO {}.'.format(score))

# GAME SETUP


# ASK THE USER FOR INPUT
game_on = True

while True:
	print('WELCOME TO MY NUMBER GUESSING GAME!\n')

	score = 100

	print('I AM THINKING OF A NUMBER IN BETWEEN 1 AND 100\n')
	print('GUESS IT CORRECTLY AND YOU WIN!\n')
	print('GOOD LUCK!\n')

	

	while game_on:
		guess = input('Enter your guess: ')

		if guess == num:
			you_win()
			replay()

		else:
			reduced_score(score)
			give_clue()

	