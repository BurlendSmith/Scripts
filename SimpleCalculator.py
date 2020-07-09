# THIS IS A SIMPLE MATH CALCULATOR THAT I MADE WHEN I WAS BORED AND HIGH.


def add_nums():
	n1 = int(input('Enter your first number: '))
	n2 = int(input('Enter your second numer: '))
	result = n1 + n2
	print('Your sum is {}.'.format(result))
	return result
def sub_nums():
	n1 = int(input('Enter your first number: '))
	n2 = int(input('Enter your second numer: '))
	result = n1 - n2
	print('Your result is {}.'.format(result))
	return result
	
def mult_nums():
	n1 = int(input('Enter your first number: '))
	n2 = int(input('Enter your second numer: '))
	result = n1 * n2
	print('Your result is {}.'.format(result))
	return result
def div_nums():
	n1 = int(input('Enter your first number: '))
	n2 = int(input('Enter your second numer: '))
	result = n1 / n2
	print('Your result is {}.'.format(result))
	return result

def replay():
	choice = input("Another one? Enter 'yes' or 'no': ")
	
	return choice == 'yes'

print('WELCOME TO SIMPLE CALCULATOR!')


while True:
	print('\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division\n')
	question = input('Enter the number of the math operation you want to perform: ')

	if question == '1':
		add_nums()
		replay()
	elif question == '2':
		sub_nums()
		replay()
	elif question == '3':
		mult_nums()
		replay()
	elif question == '4':
		div_nums()
		replay()
	
	else:
		print("Please choose from the available options.")

	if not replay():
		break
input('Press ENTER to exit')
